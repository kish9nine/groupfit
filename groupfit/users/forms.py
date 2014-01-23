from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 50)
    email = forms.EmailField()
    confirm_email = forms.EmailField()
    
    
