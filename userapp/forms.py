from django import forms
# from django.contrib.auth.models import User
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    mobile_number = forms.CharField(max_length=10)

    class Meta():
        model = User
        fields = ('username', 'password', 'email', 'mobile_number')

class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    mobile_number = forms.CharField(max_length=10)

    class Meta():
        model = User
        fields = ('username', 'password', 'email', 'mobile_number', 'is_superuser', 'is_staff', 'is_active')