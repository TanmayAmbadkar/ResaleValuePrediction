from django import forms
from SellerUI.models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SellerProfileForm(forms.ModelForm):

    first_name = forms.CharField(widget = forms.TextInput())
    last_name = forms.CharField(widget = forms.TextInput())
    username = forms.CharField(widget = forms.TextInput())
    email = forms.EmailField(widget = forms.TextInput())
    password  = forms.CharField(widget = forms.TextInput())

    class Meta():
        model = SellerProfile
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'phone_number')

class VehicleForm(forms.ModelForm):

    class Meta():

        model = Vehicle
        fields = ('Vmodel', 'make', 'desc', 'age', 'mileage',
                  'year', 'fueltank', 'price')

        widgets = {
            'desc' : SummernoteWidget()
        }
