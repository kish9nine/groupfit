from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from users.models import UserProfile
from django.contrib.auth.models import User


class RegisterForm(ModelForm):
    username = forms.CharField(
        required = True, 
        #label="USERNAME", 
        TextInput(attrs={'class':'form-control', 'placeholer':'Username'}))
        
    first_name = forms.CharField(
        required = True, 
        #label="FIRSTNAME", 
        TextInput(attrs={'class':'form-control', 'placeholer': 'Firstname'}))
        
    last_name = forms.CharField(
        required = True, 
        #label="LASTNAME", 
        TextInput(attrs={'class':'form-control', 'placeholer':'Lastname'}))
        
    password = forms.CharField(
        required = True, 
        #label="PASSWORD", 
        PasswordInput(attrs={'class':'form-control', 'placeholer':'Password'}))
        
    """confirm_password = models.CharField(
        required = True, 
        label="CONFIRM_PASSWORD", 
        PasswordInput(attrs={'class':'form-control', 'placeholer':'Confirm password'}))"""
        
    email = forms.CharField(
        required = True, 
        #label="EMAIL", 
        EmailInput(attrs={'class':'form-control', 'placeholer':'Email'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']
        
        #Labels for each field.
        label = {
            'username': 'USERNAME',
            'first_name': 'FIRSTNAME',
            'last_name': 'LASTNAME',
            'password': 'PASSWORD',
            'confirm_password': 'CONFIRM PASSWORD',
            'email': 'EMAIL',
            }
