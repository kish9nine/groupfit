from django.db import models


class Tag( models.Model ):
    """
    This model represents the tag/interest feature, which lets groups and
    users be tagged based on their interests or features.
    """

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

