from django.db import models
from django.contrib.auth.models import User
from groups.models import WorkoutGroup
from django.db.models.signals import post_save
from tags.models import Tag


class UserProfile( models.Model ):
    user = models.OneToOneField(
        User,
    )

    groups = models.ManyToManyField(
        WorkoutGroup,
        blank = True,
        related_name = "members",
    )

    tags = models.ManyToManyField(
        Tag,
        blank = True,
    )

    def __unicode__(self):
        return "%s" % self.user.username

def create_user_profile( sender, instance, created, **kwargs ):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)
