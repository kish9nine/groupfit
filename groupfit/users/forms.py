from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from users.models import UserProfile
from django.contrib.auth.models import User


class RegisterForm(ModelForm):
    class Meta:
        #This model form is based on UserProfile.
        model = User
        #These are the fields that the user will be inputing. 
        fields = ['username', 'first_name', 'last_name','password', 'email']
        
        #Labels for each field.
        label = {
            'username': 'USERNAME',
            'first_name': 'FIRST NAME',
            'last_name': 'LAST NAME',
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

    #username = forms.CharField(max_length = 20)
    #password = forms.CharField(max_length = 50)
    #email = forms.EmailField()
    #confirm_email = forms.EmailField()
    
    
