from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from playlists.models import Playlist, Track
from playlists.forms import PlaylistForm, TrackForm

@login_required
def create_playlist(request):

    # A FormSet basically allows you to have a dynamic number of the same
    # kind of form, in this case "Track" forms.
    TrackFormset = modelformset_factory(Track, TrackForm, max_num=10, extra=1)
    track_formset = TrackFormset(queryset=Track.objects.none())

    # If the user submitted the form (POST), then process it.
    if request.method == 'POST':
        # Fill out the Form object with POST variables from the user.
        playlist_form = PlaylistForm( request.POST )
        track_formset = TrackFormset( request.POST )

        # Validate the form.
        if playlist_form.is_valid() and track_formset.is_valid():

            # Construct an object from the form fields, but don't save it
            # yet, in case we want to process it some (ie. adding more
            # values to its fields).
            playlist = playlist_form.save()
            track_formset.save()

            ## Add tracks to the playlist
            for track_form in track_formset:
                if track_form.is_valid():
                    track = track_form.save()
                    if len(track.name) > 0:
                        playlist.tracks.add( track )
                    else:
                        track.delete()

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
        'track_formset' : track_formset,
    },
    )

@login_required
def delete_playlist(request, playlist_pk):
    # Get the playlist and the requesting user
    playlist = get_object_or_404( Playlist, pk=playlist_pk )
    user_playlists = request.user.userprofile.playlists.all()

    # If the user does own this playlist, remove it from the user.
    if playlist in user_playlists:
        request.user.userprofile.playlists.remove( playlist )

    return redirect('users.views.view_user', request.user.userprofile.pk)

@login_required
def view_playlist(request, playlist_pk):
    playlist = get_object_or_404( Playlist, pk=playlist_pk )
    return render(request, 'view_playlist.html', {
        'playlist': playlist,
    },
    )
