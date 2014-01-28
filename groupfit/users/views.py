from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import UserProfile, create_user_profile
from users.forms import RegisterForm, PasswordForm, EditUserProfileForm
from groupfit.forms import WorkoutGoalForm, WorkoutForm
from groupfit.models import Workout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


def create_user(request):
    #If the user is trying to add info to the server,
    if request.method == 'POST':
        #Feed as arguments to RegisterForm the inputs from the user.
        create_user_form = RegisterForm(request.POST)
        confirm_password_form = PasswordForm(request.POST)
        #If username and password are of the right length and email is of the valid form,
        #And password and confirm password identical, 
        if create_user_form.is_valid() and confirm_password_form.is_valid():
            #Don't save the user in creation as a new user yet. 
            new_user = create_user_form.save(commit=False)
            #confirm_password = confirm_password_form.save()

            pw = create_user_form.cleaned_data.get('password')
            confirm_pw = confirm_password_form.cleaned_data.get('confirm_password')
            email_overlap = User.objects.filter(email = create_user_form.cleaned_data.get('email')).exists() 
            if pw == confirm_pw and not email_overlap:
                new_user.set_password( pw )
                new_user.save()

                # This should already automatically create a UserProfile.

                ##Then create UserProfile object from User object.
                #new_UserProfile = UserProfile(user=new_user)
                ##new_UserProfile.user = new_user
                #new_UserProfile.save() #Then save. 

                #Send a welcome email. 
                send_mail('Welcome to GroupFit!', 'Welcome to GroupFit!', settings.EMAIL_HOST_USER, [new_user.email])
 
                #Render a Welcome to GroupFit page if the input info is valid. 
                #No need to customize welcome page unless we want to just switch the name: Welcome, username!
                return render(request, 'welcome.html')

    else:
        #If the user didn't plug in anything, create_user_form will be an empty shell?
        create_user_form = RegisterForm()
        confirm_password_form = PasswordForm()
    return render(request, 'register.html', {'create_user_form': create_user_form, "confirm_password_form": confirm_password_form})



@login_required
def view_user(request, user_pk=-1):
    if user_pk == -1:
        user_pk = request.user.userprofile.pk
    user = get_object_or_404( UserProfile, pk=user_pk )
    workouts = user.workout_set.all()
    completed_goals = user.goals.filter( achieved = True )


    if request.method == 'POST' and request.user == user.user:

        if 'submit-goal' in request.POST:
            goal_form = WorkoutGoalForm(request.POST, prefix="goal")
            if goal_form.is_valid():
                goal = goal_form.save(commit=False)
                goal.save()
                user.goals.add( goal )
                return redirect('users.views.view_user', user_pk)
        else:
            goal_form = WorkoutGoalForm(prefix="goal")

        if 'submit-workout' in request.POST:
            workout_form = WorkoutForm(request.POST, prefix="workout")
            if workout_form.is_valid():
                workout = workout_form.save(commit=False)
                workout.user = request.user.userprofile
                workout.save()
                return redirect('users.views.view_user', user_pk)
        else:
            workout_form = WorkoutForm(prefix="workout")
        
        if 'submit-new-profile' in request.POST:
            edit_profile_form = EditUserProfileForm(request.POST, prefix="edit")
            if edit_profile_form.is_valid():

                new_first_name = edit_profile_form.cleaned_data.get('first_name')
                new_last_name = edit_profile_form.cleaned_data.get('last_name')
                new_password = edit_profile_form.cleaned_data.get('new_password')
                confirm_password = edit_profile_form.cleaned_data.get('confirm_password')


                if len( new_first_name ) > 0:
                    request.user.first_name = new_first_name
                if len( new_last_name ) > 0:
                    request.user.last_name = new_last_name
                if len( new_password ) > 0:
                    request.user.set_password( new_password )
                request.user.save()

                #edit_profile_form.save()
                return redirect('users.views.view_user', user_pk)
        else:
            edit_profile_form = EditUserProfileForm(prefix="edit")

    else:
        goal_form = WorkoutGoalForm(prefix="goal")
        workout_form = WorkoutForm(prefix="workout")
        edit_profile_form = EditUserProfileForm(prefix="edit")

    return render(request, 'view_user.html', {
        'profile': user,
        'workouts': workouts,
        'completed_goals': completed_goals,
        'goal_form': goal_form,
        'workout_form': workout_form,
        'edit_profile_form': edit_profile_form,
    },
    )

"""
@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_user_form = EditUserProfileForm(request.POST)
"""
