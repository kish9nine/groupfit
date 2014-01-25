from django import forms
from django.forms import TextInput, EmailInput

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=20, widget = forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
