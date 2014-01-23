from django import forms


class ForgotPassword(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.CharField()
    
