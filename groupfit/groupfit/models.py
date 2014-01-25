from django.db import models


class WorkoutGoal( models.Model ):
    """
    This model represents the goal of an individual or group.
    """

    name = models.CharField(
        blank = False,
        help_text = "Name Your Goal",
        max_length = 50,
    )

    amount = models.CharField(
        blank = False,
        help_text = "How far do you need to go to achieve this goal?",
        max_length = 50,
    )

    activity = models.CharField(
        blank = False,
        help_text = "What activity does this goal use?",
        max_length = 50,
    )

    units = models.CharField(
        blank = False,
        help_text = "What type of thing does this goal describe?",
        max_length = 50,
    )

    target_date = models.DateField(
        blank = False,
    )
