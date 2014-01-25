from django import forms
from django.forms import TextInput, EmailInput

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(required=True, max_length=20, widget = forms.TextInput(attrs={'class': 'form-control', "placeholder": "Username"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', "placeholder": "Password"}))
    
