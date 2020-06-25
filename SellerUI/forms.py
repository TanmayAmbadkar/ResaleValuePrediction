from django import forms
from SellerUI.models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class VehicleForm(forms.ModelForm):

    class Meta():

        model = Vehicle
        fields = ('Vmodel', 'make', 'desc', 'mileage',
                  'year', 'fueltank', 'price')

        widgets = {
            'desc' : SummernoteWidget()
        }

class VehiclePredForm(forms.ModelForm):
    class Meta:
        model=VehiclePredPrice
        fields='__all__'
