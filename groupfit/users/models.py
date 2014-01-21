from django.db import models
from django.contrib.auth.models import User
from groups.models import WorkoutGroup
from tags.models import Tag


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
