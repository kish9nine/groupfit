from django.db import models

class Playlist( models.Model ):
    name = models.CharField(
        blank = False,
        help_text = "Name your playlist.",
        max_length = 50,
    )
