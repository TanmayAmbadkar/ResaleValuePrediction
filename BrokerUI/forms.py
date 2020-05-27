from django import forms
from django.contrib.auth.models import user
from BrokerUI.models import *

class BrokerProfileInfoForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = BrokerProfile
        fields = ('firstname', 'lastname','username', 'email', 'password','phone_number')
