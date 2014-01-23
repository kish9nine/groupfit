from django.shortcuts import render, get_object_or_404, redirect
from groups.models import WorkoutGroup
from groups.forms import GroupRegisterForm
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
    if request.method == 'POST':
        create_group_form = GroupRegisterForm(request.POST)
        if create_group_form.is_valid():

            # 0) create a group object from the form
            new_group = create_group_form.save()

            # 1) manipulate the new group

            # 2) get data about emails

            # 3) get the users corresponding to emails

            # 4) add this group to those members' rosters

            # 5) add the creating user to the groups' roster
            request.user.userprofile.groups.add( new_group )

            return redirect('groups.views.view_group', new_group.pk)

    else:
        create_group_form = GroupRegisterForm()

    return render(request, 'create_group.html', {
        'group_form': create_group_form,
    },
    )
