from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from playlists.models import Playlist

@login_required
def create_playlist(request):
    return render(request, 'create_playlist.html', {
    },
    )

def view_playlist(request, playlist_pk):
    playlist = get_object_or_404( Playlist, pk=playlist_pk )
    return render(request, 'view_playlist.html', {
        'playlist': playlist,
    },
    )
