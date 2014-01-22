from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import UserProfile

@login_required
def view_user(request, user_pk=-1):
    if user_pk == -1:
        user_pk = request.user.userprofile.pk
    user = get_object_or_404( UserProfile, pk=user_pk )
    return render(request, 'view_user.html', {
        'profile': user,
    },
    )
