from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import formset_factory
from groups.models import WorkoutGroup
from groups.forms import GroupRegisterForm, EmailForm
from users.models import UserProfile
from groupfit.forms import WorkoutGoalForm
from groupfit.models import WorkoutGoal, Workout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import datetime

@login_required
def view_group(request, group_pk):
    """
    This view simply displays the group page to the user, depending on the
    request pk.
    """

    date = datetime.date.today()
    start_of_week = date - datetime.timedelta( 7 )

    group = get_object_or_404( WorkoutGroup, pk=group_pk )
    member_workouts = {}
    for member in group.members.all():
        workouts = member.workout_set.all()
        member_workouts[member] = workouts

    if request.method == 'POST':
        goal_form = WorkoutGoalForm(request.POST)
        if goal_form.is_valid():
            goal = goal_form.save(commit=False)
            goal.save()
            group.goals.add( goal )
            return redirect('groups.views.view_group', group_pk)
    else:
        goal_form = WorkoutGoalForm()

    completed_goals = group.goals.filter(achieved=True)
    
    ## Adding new members
        if 'new-member-submit' in request.POST:
            new_member_form = EmailForm(request.POST, prefix='new')
            if new_member_form.is_valid():
                new_member_email = new_member_form.cleaned_data.get('email')
                new_member = User.objects.get(email=new_member_email)
                group.members.add(new_member)
                group.save()
                return redirect('groups.views.view_group', group_pk, {'new_member_form':new_member_form})
            
        

    return render(request, 'view_group.html', {
        'group': group,
        'goal_form' : goal_form,
        'member_workouts' : member_workouts,
        'completed_goals' : completed_goals,
        "new_member_form" : new_member_form,
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
                            member_user = User.objects.get( email = email )
                            member = UserProfile.objects.get( user=member_user )
                            new_group.members.add( member )
                            #Send email to the members who were added. 
                            send_mail('You have been invited to join ' + str(new_group.name) + ' in Groupfit!',
                                'You have been invited to join ' + str(new_group.name) + ' in Groupfit!',
                                settings.EMAIL_HOST_USER, [email])
                            
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



def complete_goal(request, group_pk, goal_pk):
    goal = get_object_or_404(WorkoutGoal, pk=goal_pk)
    group = get_object_or_404( WorkoutGroup, pk=group_pk )
    user_groups = request.user.userprofile.groups.all()

    if group in user_groups:
        if goal in group.goals.all():
            goal.achieved = True
            goal.save()
    return redirect('groups.views.view_group', group.pk)

    
