from django.db import models
from django.contrib.auth.models import User


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
        return "%s" % tag

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
            'users.views.view_group',
            args=[str(self.pk)]
        )

class UserProfile( models.Model ):
    user = models.OneToOneField(
        User,
    )

    groups = models.ManyToManyField(
        WorkoutGroup,
        related_name = "members",
    )

    tags = models.ManyToManyField(
        Tag
    )


class Trophy( models.Model ):

    name = models.CharField(
        blank = False,
        help_text = "The name of this tropy.",
        max_length = 50,
    )

    owner = models.ForeignKey(
        UserProfile,
        blank = False,
    )

    tags = models.ManyToManyField(
        Tag
    )

