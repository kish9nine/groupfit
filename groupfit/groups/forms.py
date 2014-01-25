from django import forms
from django.forms import ModelForm
from groups.models import WorkoutGroup
from django.contrib.auth.models import Group


# This form will be used in a formset, or a dynamically resizable
# collection of forms, to provide a storage point for user emails.
# Ideally, there will be some sort of master input box defined in a
# template, and JQuery can fill out these hidden forms, dynamically adding
# them as needed.
class EmailForm( forms.Form ):
    email = forms.EmailField(
        required = True,
        widget = forms.HiddenInput(),
    )

# This form will fill out a WorkoutGroup object. The members will be empty,
# but if a Formset of EmailForms is provided, we will be able to stick
# those into the WorkoutGroup model in the processing view.
class GroupRegisterForm(ModelForm):
    class Meta:

        #This model form is based on WorkoutGroup.
        model = WorkoutGroup

        # These are the fields that the user will be inputing. 
        # Note -- because 'members' is the reverse of a ManyToManyField, we
        # can't actually define it as a field. Instead, we need to separate
        # out that functionality into some logic in the view, then add this
        # new group to all the invited users.
        fields = ['name']
        exclude = ['tags']

        #Labels for each field.
        label = {
            'name': 'Name Your Group',
            #'goal_name': 'Set a Goal',
            #'goal_num': '',
            }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Group Name',
            }),
            #'goal': forms.TextInput(attrs={
            #    'class': 'form-control',
            #    'placeholder': 'Group Goal (e.g. Weight Loss)',
            #}),
        }
