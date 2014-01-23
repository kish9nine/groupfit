from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from playlists.models import Playlist
from playlists.forms import PlaylistForm, TrackForm

@login_required
def create_playlist(request):

    # If the user submitted the form (POST), then process it.
    if request.method == 'POST':
        # Fill out the Form object with POST variables from the user.
        playlist_form = PlaylistForm( request.POST )
        # Validate the form.
        if playlist_form.is_valid():
            # Construct an object from the form fields, but don't save it
            # yet, in case we want to process it some (ie. adding more
            # values to its fields).
            playlist = playlist_form.save(commit=False)
            ## add tracks to the playlist

            # Save the object.
            playlist.save()

            # Add the object to the user object's playlist list.
            user = request.user.userprofile
            user.playlists.add( playlist )

            # Finally, redirect the user.
            return redirect( 'playlists.views.view_playlist', playlist.pk )
    else:
        # If the user did not submit the form, give them an empty one.
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
