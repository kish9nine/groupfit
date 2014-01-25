from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from users.models import UserProfile
from django.contrib.auth.models import User

class RegisterForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']
        
        #Required fields. Let's see if this works. 
        required = ['username', 'first_name', 'last_name', 'password', 'email']
        
        
        #Labels for each field.
        label = {
            'username': 'USERNAME',
            'first_name': 'FIRSTNAME',
            'last_name': 'LASTNAME',
            'password': 'PASSWORD',
            'confirm_password': 'CONFIRM PASSWORD',
            'email': 'EMAIL',
            }
            
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
        }
