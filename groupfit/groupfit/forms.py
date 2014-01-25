from django import forms
from groupfit.models import WorkoutGoal

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(
        max_length = 20,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            "placeholder": "Username"
        })
    )

    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'class':'form-control',
            "placeholder": "Password"
        })
    )

class WorkoutGoalForm( forms.ModelForm ):
    class Meta:

        model = WorkoutGoal

        fields = ['name', 'amount', 'activity', 'units', 'target_date']
        exclude = []

        label = {
            'name': 'Name',
            'amount': 'Amount',
            'activity': 'Activity',
            'units': 'Units',
            'target_date': 'Target Date',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Goal Name',
            }),

            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Goal Amount',
            }),

            'activity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Goal Activity (eg. yoga, climbing)',
            }),

            'units': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Goal Units (eg. weight, miles)',
            }),

            'target_date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Target Date (eg 10/20/2014)',
            }),
