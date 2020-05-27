from django import forms
from SellerUI.models import *

class SellerProfileForm(forms.ModelForm):

    password  = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'phone_number')

class VehicleForm(forms.ModelForm):

    class Meta():

        model = Vehicle
        fields = ('Vmodel', 'make', 'description', 'age', 'mileage',
                  'year', 'fueltank', 'price')

        widgets = {
            'description' : SummernoteWidget()
        }
