from django import forms
from BrokerUI.models import Profile,Estate,Prediction
from django.contrib.auth.models import User
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['type','phone_number']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password' )

class EsateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = ['lat','lon','bedroom','bathroom','carpetarea','builtuparea','price']

class PredictionForm(forms.ModelForm):
    class Meta:
        model=Prediction
        fields='__all__'