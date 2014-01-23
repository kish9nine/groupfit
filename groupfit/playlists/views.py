from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from playlists.models import Playlist
from playlists.forms import PlaylistForm, TrackForm

@login_required
def create_playlist(request):
    if request.method == 'POST':
        playlist_form = PlaylistForm( request.POST )
        if playlist_form.is_valid():
            playlist = playlist_form.save(commit=False)
            ## add tracks to the playlist
            playlist.save()
            user = request.user.userprofile
            user.playlists.add( playlist )
            return redirect( 'playlists.views.view_playlist', playlist.pk )
    else:
        playlist_form = PlaylistForm()

    return render(request, 'create_playlist.html', {
        'playlist_form': playlist_form,
    },
    )

def view_playlist(request, playlist_pk):
    playlist = get_object_or_404( Playlist, pk=playlist_pk )
    return render(request, 'view_playlist.html', {
        'playlist': playlist,
    },
    )
