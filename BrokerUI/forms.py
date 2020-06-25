from django import forms
from BrokerUI.models import Profile,Estate,Prediction
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['type','phone_number']

class UserForm(forms.ModelForm):

    password  = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password' )

class EstateForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = ['lat','lon','bedroom','bathroom','carpetarea','builtuparea','price']

class PredictionForm(forms.ModelForm):
    class Meta:
        model=Prediction
        fields='__all__'

class QueryForm(forms.Form):
    broker_name = forms.CharField(label="Broker's name",max_length=100,required=False)
    min_cost = forms.FloatField(label="Min cost",required=False)
    max_cost = forms.FloatField(label="Max cost",required=False)
