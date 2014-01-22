from django.shortcuts import render, get_object_or_404
from groups.models import WorkoutGroup
from django.contrib.auth.decorators import login_required

def view_group(request, group_pk=-1):
    """
    This view simply displays the group page to the user, depending on the
    request pk.
    """

    group = get_object_or_404( WorkoutGroup, pk=group_pk )
    return render(request, 'view_group.html', {
        'group': group,
    },
    )

@login_required
def create_group(request):
    """
    This view presents the user with a form which lets them create a new
    group.
    """

    return render(request, 'create_group.html', {
    },
    )
