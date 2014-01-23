from django.db import models
from django.core.urlresolvers import reverse


class Track( models.Model ):
    name = models.CharField(
        blank = False,
        help_text = "Track title.",
        max_length = 100,
    )

    def __unicode__(self):
        return "%s" % self.name

class Playlist( models.Model ):
    name = models.CharField(
        blank = False,
        help_text = "Name your playlist.",
        max_length = 50,
    )

    tracks = models.ManyToManyField(
        Track,
        blank = True,
        help_text = "Your playlist's tracks.",
    )

    def __unicode__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse(
            'playlists.views.view_playlist',
            args=[str(self.pk)]
        )
