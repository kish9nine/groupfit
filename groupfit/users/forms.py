from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from users.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class PasswordForm(forms.Form):
    confirm_password = forms.CharField(
        required = True, 
        label="CONFIRM_PASSWORD", 
        widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password', 'onchange':'checkPass()'}))
    

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
        widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Password','onchange':'checkPass()'})
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
class EditUserProfileForm:
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
        widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Reset password',})
        )
        
    email = forms.EmailField(
        required = True, 
        label="EMAIL", 
        widget=EmailInput(attrs={'class':'form-control', 'placeholder':'Email'})
        )
        
    class Meta:
        model = UserProfile.user
        fields = ['username', 'first_name', 'last_name', 'password', 'email']
        
