from django import forms
from SellerUI.models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class UserForm(forms.ModelForm):

    password  = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password' )

class ProfileForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = ('phone_number', 'type', )

class VehicleForm(forms.ModelForm):

    class Meta():

        model = Vehicle
        fields = ('Vmodel', 'make', 'desc', 'age', 'mileage',
                  'year', 'fueltank', 'price')

        widgets = {
            'desc' : SummernoteWidget()
        }
