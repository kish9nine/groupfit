from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class PasswordForm(forms.Form):
    confirm_password = forms.CharField(
        required = False, 
        label="CONFIRM_PASSWORD", 
        widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password', 'onkeydown':'checkPass()'}))
    

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
        widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Password','onkeydown':'checkPass()'})
        )
        
    email = forms.EmailField(
        required = True, 
        label="EMAIL", 
        widget=EmailInput(attrs={'class':'form-control', 'placeholder':'Email'})
        )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']
       
       
    """
    def clean(self):
        pw1 = self.cleaned_data.get('password')
        pw2 = self.cleaned_data.get('confirm_password')
        
        if pw1 != pw2:
            raise forms.ValidationError('Passwords do not match!')
        return pw2
    """


#@login_required
#I am not sure if I should add login_required here. 
# nope! only used in views :)
class EditUserProfileForm(forms.ModelForm):
    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'password']
        exclude = ['username', 'email'] #These data should not be altered. 

        label = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'new_password': 'New Password',
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Reset Your First Name.'
                }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Reset Your Last Name.'
                }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder': 'Reset Your Password.'
                }) 
        }


