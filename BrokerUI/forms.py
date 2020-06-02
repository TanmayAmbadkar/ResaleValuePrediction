from django import forms
from myapp.models import Profile,Estate
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