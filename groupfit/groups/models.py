from django.db import models
from tags.models import Tag


class WorkoutGroup( models.Model ):

    name = models.CharField(
        blank = False,
        help_text = "The name of your workout group.",
        max_length = 50,
    )

    tags = models.ManyToManyField(
        Tag
    )

    def __unicode__(self):
        return "Workout Group %s" % self.pk

    def get_absolute_url(self):
        return reverse(
            'groups.views.view_group',
            args=[str(self.pk)]
        )

