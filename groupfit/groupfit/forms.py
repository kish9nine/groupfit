from django import forms


class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.CharField()
    
