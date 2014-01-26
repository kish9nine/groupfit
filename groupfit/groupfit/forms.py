from django import forms
from groupfit.models import WorkoutGoal
from django.contrib.auth.forms import PasswordResetForm

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(
        required = True,
        max_length = 20,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            "placeholder": "Username",
        })
    )

    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput(attrs={
            'class':'form-control',
            "placeholder": "Email"
        })
    )
    
    new_pw = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password', 
            })
        )
    confirm_new_pw = forms.CharField(
        required = True,
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password',
            }))

            

class WorkoutGoalForm( forms.ModelForm ):
    class Meta:
        model = WorkoutGoal

        fields = [
            'name',
            'amount',
            'activity',
            'units',
            'target_date',
            'description'
        ]
        exclude = []

        label = {
            'name': 'Goal Nickname',
            'amount': 'Goal Amount',
            'activity': 'Activity',
            'target_date': 'Target Completion Date',
            'description': 'Goal Description',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Goal Nickname',
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Goal Amount',
            }),
            'activity': forms.HiddenInput(),
            'units': forms.HiddenInput(),
            'target_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Target Date (eg. 10/20/2014)',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Goal Description',
                'rows': 3,
            }),
        }


