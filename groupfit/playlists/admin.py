from django.contrib import admin
from playlists.models import Playlist, Track

admin.site.register( Playlist )
admin.site.register( Track )
