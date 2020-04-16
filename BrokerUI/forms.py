from django import forms
from django.contrib.auth.models import user
from BrokerUI.models import *

class BrokerForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('firstname', 'lastname','username', 'email', 'password')

class BrokerProfileInfo(forms.ModelForm):

    class Meta():
        model = BrokerProfile
        fields = ('phone_number')
