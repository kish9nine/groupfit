from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import formset_factory
from groups.models import WorkoutGroup
from groups.forms import GroupRegisterForm, EmailForm
from groupfit.forms import WorkoutGoalForm
from groupfit.models import WorkoutGoal
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail

@login_required
def view_group(request, group_pk):
    """
    This view simply displays the group page to the user, depending on the
    request pk.
    """

    group = get_object_or_404( WorkoutGroup, pk=group_pk )

    if request.method == 'POST':
        goal_form = WorkoutGoalForm(request.POST)
        if goal_form.is_valid():
            goal = goal_form.save(commit=False)
            goal.save()
            group.goals.add( goal )
            return redirect('groups.views.view_group', group_pk)
    else:
        goal_form = WorkoutGoalForm()

    return render(request, 'view_group.html', {
        'group': group,
        'goal_form' : goal_form,
    },
    )


@login_required
def leave_group(request, group_pk):
    group = get_object_or_404( WorkoutGroup, pk=group_pk )
    user_groups = request.user.userprofile.groups.all()

    if group in user_groups:
        request.user.userprofile.groups.remove( group )

    return redirect('groups.views.view_group', group.pk)

@login_required
def create_group(request):
    """
    This view presents the user with a form which lets them create a new
    group.
    """

    EmailFormset = formset_factory(EmailForm, max_num=10, extra=1)

    if request.method == 'POST':
        create_group_form = GroupRegisterForm(request.POST)
        email_formset = EmailFormset(request.POST)
        if create_group_form.is_valid() and email_formset.is_valid():

            # 1) create a group object from the form
            new_group = create_group_form.save()

            # 2) get data about emails, add them to roster
            for email_form in email_formset:
                if email_form.is_valid():
                    email = email_form.cleaned_data.get('email')
                    if email and len(email) > 0:
                        try:
                            member = User.objects.get( email = email )
                            new_group.members.add( member.userprofile )
                            #Send email to the members who were added. 
                            #Is this the right place to write send_mail?
                            
                        except (User.DoesNotExist, User.MultipleObjectsReturned) as e:
                            pass

            # 3) add the creating user to the groups' roster
            request.user.userprofile.groups.add( new_group )

            return redirect('groups.views.view_group', new_group.pk)

    else:
        create_group_form = GroupRegisterForm()
        email_formset = EmailFormset()

    return render(request, 'create_group.html', {
        'group_form': create_group_form,
        'email_formset': email_formset,
    },
    )

def join_group(request, group_pk):
    group = get_object_or_404( WorkoutGroup, pk=group_pk )
    group.members.add( request.user.userprofile )
    return redirect('groups.views.view_group', group_pk)
