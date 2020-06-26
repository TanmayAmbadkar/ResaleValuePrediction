from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from SellerUI.models import *
from BrokerUI.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.decorators import login_required
from SellerUI.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
import joblib
import pandas as pd
import numpy as np
from django.contrib import messages
# Create your views here.

# Create your views here.

class HomeView(TemplateView):
    template_name = 'SellerUI/home.html'

class ContributorView(TemplateView):
    template_name = 'SellerUI/aboutus.html'

class CreateVehicleView(LoginRequiredMixin, CreateView):

    template_name = 'SellerUI/vehicle_form.html'
    success_url = reverse_lazy('home')
    login_url = '/login/'
    form_class = VehicleForm
    model = Vehicle

    def form_valid(self, form):
        profile = Profile.objects.get_or_create(user = self.request.user)[0]
        print(profile)
        form.instance.seller = profile
        print(form.instance.photo)
        form.instance.publish()
        form.instance.save()
        return super().form_valid(form)


class VehicleUpdateView(LoginRequiredMixin, UpdateView):

    #The update view just changes the parameters of an already created object.
    # We specify <int:pk> in the url to get the specific object to update

    template_name = 'SellerUI/vehicle_form.html'
    success_url = reverse_lazy('vehicle_draft_list')
    login_url = '/login/'
    form_class = VehicleForm
    model = Vehicle

class VehicleDetailView(DetailView):

    #Simply sends a single object pk = <int:pk> to the page.
    #the context dict is a single object, which could be changed using get_context_data

    model = Vehicle

class VehicleListView(ListView):
    #Simply sends all objects of the model to page.
    #the context dict is aall objects, which could be changed using get_context_data

    model = Vehicle
    paginate_by=10


class DraftListView(LoginRequiredMixin, ListView):

    #to get the draft vehicles only for the seller that has requested it
    #I have selected the profile from the request.user, then selected all vehicle
    # objects made by that user and send it to the context_dict

    login_url = '/login/'
    model = Vehicle
    template_name = 'SellerUI/vehicle_draft_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        profile = Profile.objects.filter(user = self.request.user)[0]
        return Vehicle.objects.filter(seller = profile)

def VehiclePricePrediction(request):
    if request.method=='POST':
        form=VehiclePredForm(request.POST)
        if form.is_valid():
            mydict=(request.POST).dict()
            df = pd.DataFrame(mydict,index=[0])
            df['Year'] = int(df['Year'])
            df['mileage'] = int(df['mileage'])
            df.drop('csrfmiddlewaretoken', axis = 1, inplace = True)
            dumm = pd.get_dummies(df)
            if 'Make_audi' in dumm.columns:
                dumm.drop('Make_audi', axis = 1, inplace = True)

            if 'Model_3-series' in dumm.columns:
                dumm.drop('Model_3-series', axis = 1, inplace = True)

            if 'Type_cng' in dumm.columns:
                dumm.drop('Type_cng', axis = 1, inplace = True)

            true_labels = pd.read_csv('SellerUI/cars_final_labels.csv')
            true_labels.fillna(0, inplace = True)
            for i in dumm.columns:
                true_labels[i] = dumm[i]
            true_labels.to_csv('test.csv')
            value = processing(true_labels)
            value = value - value%1000
            print("price: ", value);
            messages.success(request,value)

    form=VehiclePredForm()
    return render(request,'SellerUI/predform.html',{'form':form})

def processing(df):
    regressor = joblib.load('SellerUI/MLModel.pkl')
    scaler=joblib.load('SellerUI/scaler.pkl')
    print(df.shape)
    X = scaler.transform(df)
    output = regressor.predict(df)
    return int(output)


'''
class CreateUserView(CreateView):

    #Creates new user, no profile.
    #To set password, i have to use the set_password method

    template_name = 'SellerUI/user_form.html'
    form_class = UserForm
    model = User
    def form_valid(self, form):

        form.instance.set_password(form.instance.password)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        form.instance.save()
        login(self.request, form.instance)
        return redirect('profile_new')

class CreateProfileView(CreateView):

    #This is second step in registration, which sets the profile, whether customer,
    # buyer or seller. Form has options available.
    # I have to set the foreign key so I am getting the user who is registering and
    # attaching it to the foreign key

    template_name = 'SellerUI/profile_form.html'
    success_url = reverse_lazy('home')
    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):

        #form.instance.user = User.objects.filter(username = self.request.user.username)[0]
        form.instance.user =self.request.user
        return super().form_valid(form)

class ProfileDetailView(DetailView, LoginRequiredMixin):

    model = Profile
    login_url = '/login/'
'''
