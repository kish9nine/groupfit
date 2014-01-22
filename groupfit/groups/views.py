from django.shortcuts import render, get_object_or_404
from groups.models import WorkoutGroup
from django.contrib.auth.decorators import login_required

def view_group(request, group_pk=-1):
    group = get_object_or_404( WorkoutGroup, pk=group_pk )
    return render(request, 'group_profile.html', {
        'group': group,
    },
    )

@login_required
def create_group(request):
    return render(request, 'group_create.html', {
    },
    )
