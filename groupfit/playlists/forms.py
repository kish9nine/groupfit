from django import forms
from django.forms import ModelForm, TextInput
from playlists.models import Playlist, Track

class PlaylistForm( ModelForm ):
    class Meta:
        model = Playlist
        fields = ['name', 'tracks']
        exclude = []
        labels = {
            'name': 'Name',
            'tracks': 'Tracks',
        }
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
