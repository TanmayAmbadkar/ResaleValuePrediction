from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from BrokerUI.forms import ProfileForm,UserForm,EstateForm,PredictionForm
from BrokerUI.models import Profile,Estate,Prediction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login
from BrokerUI.serializers import PredictionSerializers
import joblib
import pandas as pd
import numpy as np
from django.contrib import messages


class ProfileListView(ListView):
    model = Profile

class ProfileCreateView(LoginRequiredMixin,CreateView):
    form_class=ProfileForm
    login_url = '/login/'
    redirect_field_name = 'BrokerUI/profile_form.html'

    model = Profile
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # t=form.save(commit=False)
        # print(t)
        print(self.request.user.username)
        print(form.instance.type)
        form.instance.user = User.objects.filter(username=self.request.user.username)[0]
        username = self.request.user.username
        password = self.request.user.password
        print(username,password)
        form.instance.save()
        # t=form.save()
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            messages.error(self.request,message='Profile already created')
            return super().form_invalid(form)

class CreateUserView(CreateView):

    template_name = 'BrokerUI/user_form.html'
    success_url = reverse_lazy('new_profile')
    form_class = UserForm
    model = User
    def form_valid(self, form):

        form.instance.set_password(form.instance.password)
        valid = super(CreateUserView,self).form_valid(form)
        username,password = form.cleaned_data.get('username'),form.cleaned_data.get('password')
        new_user = authenticate(username=username,password=password)
        login(self.request,new_user)
        return valid

class CreateEstateForm(CreateView):
    template_name = 'BrokerUI/estate_form.html'
    success_url = reverse_lazy('home')
    form_class = EstateForm
    model = Estate

    def form_valid(self,form):
        p=Profile.objects.filter(user = self.request.user)[0]
        print(p.user.first_name)
        print(form.instance.price)
        form.instance.broker = p
        print(form.instance.broker.user.username)
        if(form.instance.broker.type != 'B'):
            messages.error(self.request,message='Only brokers can register')
            return super().form_invalid(form)
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            return HttpResponse(e.__cause__)

class EstateListView(ListView):
    model = Estate
    paginate_by=5

class EstateDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'BrokerUI/estate_detail.html'
    model = Estate


class EstateUpdateView(UpdateView):
    model = Estate
    template_name = 'BrokerUI/estate_update_form.html'
    form_class = EstateForm


class BrokerDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    # print(Test.pk)
    template_name= 'BrokerUI/broker_detail.html'

class BrokerUpdateView(UpdateView):
    model = Profile
    fields=['phone_number']
    template_name = 'BrokerUI/broker_update.html'

class EstateDeleteView(DeleteView):
    model = Estate
    template_name = 'BrokerUI/estate_delete.html'
    success_url = reverse_lazy('home')


def processing(df):
    regressor = joblib.load('BrokerUI/regressor_model.pkl')
    scalar_for_params=joblib.load('BrokerUI/scalar_for_params.pkl')
    scalar_for_price=joblib.load('BrokerUI/scalar_for_price.pkl')
    one_hot_encoder=joblib.load('BrokerUI/one_hot_encoder.pkl')
    columns_to_fit=['spell','sublocality_level','rooms','bathrooms','furnished','constructionstatus','project','type']
    t=pd.DataFrame(one_hot_encoder.transform(df[columns_to_fit]))
    df.drop(columns_to_fit,axis=1,inplace=True)
    df=pd.concat([df,t],axis=1)
    columns_to_scale = ['lat', 'long', 'ft', 'carpetarea']
    df[columns_to_scale]=scalar_for_params.transform(df[columns_to_scale])
    df.drop(['lat','long'],axis=1,inplace=True)
    output = regressor.predict(df)
    return scalar_for_price.inverse_transform(output)


def EstatePricePrediction(request):
    if request.method=='POST':
        form=PredictionForm(request.POST)
        if form.is_valid():
            mydict=(request.POST).dict()
            df = pd.DataFrame(mydict,index=[0])
            columns_to_fit=['spell','sublocality_level','rooms','bathrooms','furnished','constructionstatus','project','type']
            df['rooms']=np.float64(df['rooms'])
            df['bathrooms']=np.float64(df['bathrooms'])
            df=df.loc[:,'spell':]
            print(df['rooms'].dtype)
            # print(df['spell'])
            output = processing(df)
            messages.success(request,'Output Status: Rs {}'.format(np.round(output[0],2)))


    form=PredictionForm()
    return render(request,'BrokerUI/predform.html',{'form':form})

def query(request):
    qs = Estate.objects.all()
    broker_firstname_query = request.GET.get('broker_firstname_contains')
    broker_lastname_query = request.GET.get('broker_lastname_contains')
    project_name_query = request.GET.get('project')
    min_price_query,max_price_query,min_bedroom,max_bedroom,min_bathroom,max_bathroom,min_carpetarea,max_carpetarea,min_floorarea,max_floorarea = request.GET.get('min_price'),request.GET.get('max_price'),request.GET.get('min_bedroom'),request.GET.get('max_bedroom'),request.GET.get('min_bathroom'),request.GET.get('max_bathroom'),request.GET.get('min_carpetarea'),request.GET.get('max_carpetarea'),request.GET.get('min_floorarea'),request.GET.get('max_floorarea')
    if broker_firstname_query !='' and broker_firstname_query is not None:
        qs = qs.filter(broker__user__first_name__icontains=broker_firstname_query)
    if broker_lastname_query !='' and broker_lastname_query is not None:
        qs = qs.filter(broker__user__last_name__icontains=broker_lastname_query)
    if min_price_query != '' and min_price_query is not None:
        qs = qs.filter(price__gte = float(min_price_query))
    if max_price_query != '' and max_price_query is not None:
        qs = qs.filter(price__lte = float(max_price_query))
    if min_bedroom != '' and min_bedroom is not None:
        qs = qs.filter(bedroom__gte = float(min_bedroom))
    if max_bedroom != '' and max_bedroom is not None:
        qs = qs.filter(bedroom__lte = float(max_bedroom))
    if min_bathroom != '' and min_bathroom is not None:
        qs = qs.filter(bathroom__gte = float(min_bathroom))
    if max_bathroom != '' and max_bathroom is not None:
        qs = qs.filter(bathroom__lte = float(max_bathroom))
    if min_carpetarea != '' and min_carpetarea is not None:
        qs = qs.filter(carpetarea__gte=float(min_carpetarea))
    if max_carpetarea != '' and max_carpetarea is not None:
        qs = qs.filter(carpetarea__lte=float(max_carpetarea))
    if min_floorarea != '' and min_floorarea is not None:
        qs = qs.filter(builtuparea__gte=float(min_floorarea))
    if max_floorarea != '' and max_floorarea is not None:
        qs = qs.filter(builtuparea__lte=float(max_floorarea))


    context={
        'queryset':qs
    }
    return render(request,'BrokerUI/query.html',context)
