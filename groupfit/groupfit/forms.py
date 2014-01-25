from django import forms
from django.forms import TextInput, EmailInput

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(blank=False, max_length=20, widget = forms.TextInput(attrs={'class': 'form-control', "placeholder": "Username"}))
    email = forms.EmailField(blank=False, widget=forms.EmailInput(attrs={'class':'form-control', "placeholder": "Password"}))
    
