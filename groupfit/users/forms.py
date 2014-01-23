from django import forms
from django.forms import ModelForm
from users.models import UserProfile


class RegisterForm(ModelForm):
    class Meta:
        #This model form is based on UserProfile.
        model = UserProfile.user
        #These are the fields that the user will be inputing. 
        fields = ['username', 'password', 'confirm_password', 'email']
        
        #Labels for each field.
        label = {
            'username': 'USERNAME',
            'password': 'PASSWORD',
            'confirm_password': 'CONFIRM PASSWORD',
            'email': 'EMAIL',
            }
        
        
    #username = forms.CharField(max_length = 20)
    #password = forms.CharField(max_length = 50)
    #email = forms.EmailField()
    #confirm_email = forms.EmailField()
    
    
