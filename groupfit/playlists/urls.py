from django.conf.urls import patterns, include, url
from playlists.views import create_playlist, view_playlist, delete_playlist
from playlists.views import share_playlist

urlpatterns = patterns('',

    url(r'^create/$', create_playlist),
    url(r'^delete/(?P<playlist_pk>\d+)$', delete_playlist),
    url(r'^share/(?P<playlist_pk>\d+)/with/(?P<group_pk>\d+)$', share_playlist),
    url(r'^(?P<playlist_pk>\d+)$', view_playlist),

)
