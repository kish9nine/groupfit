from django.db import models
from django.core.urlresolvers import reverse
from tags.models import Tag
from groupfit.models import WorkoutGoal


class WorkoutGroup( models.Model ):
    """
    This model represents a group of individuals. It should contain all the
    information needed to manage and display their progress.
    """

    name = models.CharField(
        blank = False,
        help_text = "The name of your workout group.",
        max_length = 50,
    )

    goal = models.ManyToManyField(
        WorkoutGoal,
        null = True,
        blank = True,
        help_text = "Your Group Goal (e.g. Weight Loss)",
        related_name = "groups",
    )

    tags = models.ManyToManyField(
        Tag,
        blank = True,
        related_name = "groups",
    )

    def __unicode__(self):
        return "Workout Group %s" % self.pk

    def get_absolute_url(self):
        return reverse(
            'groups.views.view_group',
            args=[str(self.pk)]
        )

"""
This post_save function is triggered when Group object is created,
creating a WorkoutGroup object along with it.
"""
#def create_group_profile( sender, instance, created, **kwargs ):
#    if created:
#        WorkoutGroup.objects.create(group=instance)
#post_save.connect(create_group_profile, sender=User)
