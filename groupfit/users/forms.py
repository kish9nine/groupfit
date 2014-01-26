from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from users.models import UserProfile
from django.contrib.auth.models import User

class RegisterForm(ModelForm):

    username = forms.CharField(
        required = True, 
        label="USERNAME", 
        widget=TextInput(attrs={'class':'form-control', 'placeholder':'Username'})
        )
        
    first_name = forms.CharField(
        required = True, 
        label="FIRSTNAME", 
        widget=TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'})
        )
        
    last_name = forms.CharField(
        required = True, 
        label="LASTNAME", 
        widget=TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'})
        )
        
    password = forms.CharField(
        required = True, 
        label="PASSWORD", 
        widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
        )
        
    confirm_password = forms.CharField(
        required = True, 
        label="CONFIRM_PASSWORD", 
        widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password'}))
        
    email = forms.EmailField(
        required = True, 
        label="EMAIL", 
        widget=EmailInput(attrs={'class':'form-control', 'placeholder':'Email'})
        )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password', 'email']
        
       

    def clean(self):
        pw1 = self.cleaned_data['password']
        pw2 = self.cleaned_data['confirm_password']
        
        if pw1 != pw2:
            raise forms.ValidationError('Passwords do not match!')
        return pw2
