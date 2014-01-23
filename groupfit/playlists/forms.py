from django import forms
from django.forms import ModelForm, TextInput
from playlists.models import Playlist, Track

# This form is a "ModelForm" meaning it fills out an existing Model
class PlaylistForm( ModelForm ):
    class Meta:
        # The model this form refers to
        model = Playlist
        # The fields of the model we're going to use
        fields = ['name', 'tracks']
        # And fields we don't want to use
        exclude = []
        # Lables for each field, if you want any.
        labels = {
            'name': 'Name',
            'tracks': 'Tracks',
        }
        # A Widget is an HTML object. Check the documentation for more.
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Playlist Name',
            }),
        }


class TrackForm( ModelForm ):
    class Meta:
        model = Track
        fields = ['name']
        exclude = []
        labels = {
            'name': 'Track name',
        }
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Track Title',
            }),
        }
