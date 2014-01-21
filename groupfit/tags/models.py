from django.db import models


class Tag( models.Model ):

    tag = models.CharField(
        blank = False,
        help_text = "A short description of the topic.",
        max_length = 12,
    )

    description = models.CharField(
        blank = True,
        help_text = "An optional description of the tag.",
        max_length = 50,
    )

    def __unicode__(self):
        return "%s" % self.tag

