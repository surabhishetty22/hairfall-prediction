# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

        
class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')