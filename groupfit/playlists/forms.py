from django import forms
from django.forms import ModelForm, TextInput
from playlists.models import Playlist, Track

# This form is a "ModelForm" meaning it fills out an existing Model
class PlaylistForm( ModelForm ):
    class Meta:
        # The model this form refers to
        model = Playlist
        # The fields of the model we're going to use
        fields = ['name']
        # And fields we don't want to use
        exclude = ['tracks']
        # Lables for each field, if you want any.
        labels = {
            'name': 'Playlist Name',
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
        fields = ['name', 'artist', 'album']
        exclude = []
        labels = {
            'name': 'Track Title',
            'artist': 'Track Artist',
            'album': 'Track Album',
        }
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Track Title',
            }),
            'artist': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Track Artist',
            }),
            'album': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Track Album',
            }),
        }
