from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from users.models import UserProfile
from django.contrib.auth.models import User

class RegisterForm(ModelForm):

    username = forms.CharField(
        required = True, 
        label="USERNAME", 
        widget=TextInput(attrs={'class':'form-control', 'placeholer':'Username'})
        )
        
    first_name = forms.CharField(
        required = True, 
        label="FIRSTNAME", 
        widget=TextInput(attrs={'class':'form-control', 'placeholer': 'Firstname'})
        )
        
    last_name = forms.CharField(
        required = True, 
        label="LASTNAME", 
        widget=TextInput(attrs={'class':'form-control', 'placeholer':'Lastname'})
        )
        
    password = forms.CharField(
        required = True, 
        label="PASSWORD", 
        widget=PasswordInput(attrs={'class':'form-control', 'placeholer':'Password'})
        )
        
    """confirm_password = models.CharField(
        required = True, 
        label="CONFIRM_PASSWORD", 
        PasswordInput(attrs={'class':'form-control', 'placeholer':'Confirm password'}))"""
        
    email = forms.EmailField(
        required = True, 
        label="EMAIL", 
        widget=EmailInput(attrs={'class':'form-control', 'placeholer':'Email'})
        )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']
        
       
