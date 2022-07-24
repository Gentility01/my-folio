from dataclasses import fields
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForms(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your Username',
    }))
    email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Your Email',
    }))
    phone = forms.CharField(max_length=50, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Your Phone',
    }))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Your Password',
    }))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Repeat Password',
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email','phone', 'password1', 'password2']

