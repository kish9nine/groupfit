from django.conf.urls import patterns, include, url
from playlists.views import create_playlist, view_playlist

urlpatterns = patterns('',

    url(r'^create/$', create_playlist),
    url(r'^(?P<playlist_pk>\d+)$', view_playlist),

)
