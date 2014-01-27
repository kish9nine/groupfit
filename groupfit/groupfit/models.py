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

    description = models.CharField(
        blank = True,
        help_text = "Describe your goal.",
        max_length = 400,
    )

    target_date = models.DateField(
        blank = False,
    )

    def __unicode__(self):
        return "%s" % self.name


class Workout( models.Model ):
    """
    This model represents a single workout log for an individual. The
    individual makes a workout log, then these are aggregated to indicate
    "progress".
    """

    user = models.ForeignKey(
        'users.UserProfile',
        null = False,
    )

    """
    These fields are mandatory; quantifiable.
    """

    date = models.DateField(
        blank = False,
    )

    amount = models.CharField(
        blank = False,
        help_text = "How much did you workout?",
        max_length = 50,
    )

    activity = models.CharField(
        blank = False,
        help_text = "What activity were you performing?",
        max_length = 50,
    )

    units = models.CharField(
        blank = False,
        help_text = "What type of thing does this workout describe?",
        max_length = 50,
    )


    """
    These fields are optional; subjective.
    """

    description = models.CharField(
        blank = True,
        help_text = "Describe your workout",
        max_length = 400,
    )

    energy_level = models.CharField(
        blank = True,
        help_text = "Describe your energy level during this workout.",
        max_length = 50,
    )


    def __unicode__(self):
        return "%s" % self.name
