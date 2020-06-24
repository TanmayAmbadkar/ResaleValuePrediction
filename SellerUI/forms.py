from django import forms
from SellerUI.models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class VehicleForm(forms.ModelForm):

    class Meta():

        model = Vehicle
        fields = ('Vmodel', 'make', 'desc', 'age', 'mileage',
                  'year', 'fueltank', 'price')

        widgets = {
            'desc' : SummernoteWidget()
        }
