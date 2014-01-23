from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from groups.models import GroupProfile
from django.contrib.auth.models import Group


class GroupRegisterForm(ModelForm):
    class Meta:
        #This model form is based on GroupProfile.
        model = Group
        #These are the fields that the user will be inputing. 
        fields = ['groupname', 'group_goal', 'goal_num', 'email1','email2', 'email3']
        #group_num is the e.g. 50 miles for group_goal of running
        
        #Labels for each field.
        label = {
            'groupname': 'GROUPNAME',
            'group_goal': 'GROUPGOAL',
            'goal_num': 'GOALNUM',
            'email1': 'EMAIL1,
            'email2': 'EMAIL2',
            'email3': 'EMAIL3',
            }

        widgets = {
            'groupname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Groupname',
            }),
            'group_goal': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Group Goal (e.g. Weight Loss)',
            }),
            'goal_num': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Goal Number (e.g. 10 lbs) ',
            #how to handle units?
            
            }),
            'email1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email of Member 1',
            }),
            'email2': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email of Member 2',
            }),
            
            'email3': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email of Member 3',
            }),
            
            #think of how to add more emails/ how to pop up users
        }

    #groupname = forms.CharField(max_length = 20)
    #group_goal = forms.CharField(max_length = 50)
    #email = forms.EmailField()
