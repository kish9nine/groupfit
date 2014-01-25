from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from users.models import UserProfile
from django.contrib.auth.models import User


class RegisterForm(ModelForm):
    username = models.CharField(
        required = True, 
        label="USERNAME", 
        TextInput(attrs={'class':'form-control', 'placeholer':'Username'}))
        
    first_name = models.CharField(
        required = True, 
        label="FIRSTNAME", 
        TextInput(attrs={'class':'form-control', 'placeholer': 'Firstname'}))
        
    last_name = models.CharField(
        required = True, 
        label="LASTNAME", 
        TextInput(attrs={'class':'form-control', 'placeholer':'Lastname'}))
        
    password = models.CharField(
        required = True, 
        label="PASSWORD", 
        PasswordInput(attrs={'class':'form-control', 'placeholer':'Password'}))
        
    confirm_password = models.CharField(
        required = True, 
        label="CONFIRM_PASSWORD", 
        PasswordInput(attrs={'class':'form-control', 'placeholer':'Confirm password'}))
        
    email = models.CharField(
        required = True, 
        label="EMAIL", 
        EmailInput(attrs={'class':'form-control', 'placeholer':'Email'}))
    
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
    
