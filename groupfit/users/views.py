from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import UserProfile, create_user_profile
from users.forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings


def create_user(request):
    #If the user is trying to add info to the server,
    if request.method == 'POST':
        #Feed as arguments to RegisterForm the inputs from the user.
        create_user_form = RegisterForm(request.POST)
        #If username and password are of the right length and email is of the valid form,
        #And password and confirm password identical, 
        if create_user_form.is_valid():
            #Don't save the user in creation as a new user yet. 
            new_user = create_user_form.save()
            pw = create_user_form.cleaned_data.get('password')
            new_user.set_password( pw )
            new_user.save()
 
            #Then create UserProfile object from User object.
            new_UserProfile = UserProfile(user=new_user)
            #new_UserProfile.user = new_user
            new_UserProfile.save() #Then save. 
 
            #Send a welcome email. 
            send_email('Welcome to GroupFit!', 'Welcome to GroupFit!', settings.EMAIL_HOST_USER, [user.email])
 
            #Render a Welcome to GroupFit page if the input info is valid. 
            #No need to customize welcome page unless we want to just switch the name: Welcome, username!
            return render(request, 'welcome.html')
 
    else:
        #If the user didn't plug in anything, create_user_form will be an empty shell?
        create_user_form = RegisterForm()
    return render(request, 'register.html', {'create_user_form': create_user_form})
 
 

@login_required
def view_user(request, user_pk=-1):
    if user_pk == -1:
        user_pk = request.user.userprofile.pk
    user = get_object_or_404( UserProfile, pk=user_pk )
    return render(request, 'view_user.html', {
        'profile': user,
    },
    )
