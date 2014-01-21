from django.db import models
from users.models import UserProfile
from tags.models import Tag


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

