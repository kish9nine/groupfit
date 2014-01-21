from django.shortcuts import render, get_object_or_404
from groups.models import WorkoutGroup

def view_group(request, group_pk=-1):
    group = get_object_or_404( WorkoutGroup, pk=group_pk )
    return render(request, 'group_profile.html', {
        'group': group,
    },
    )
