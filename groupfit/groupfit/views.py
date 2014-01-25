from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.contrib.auth.forms import PasswardResetForm
from django.core.mail import send_mail
from groupfit.forms import ForgotPasswordForm, PasswordResetForm
from groups.models import WorkoutGroup
from users.models import UserProfile
from tags.models import Tag
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

def landing_page(request):
    """
    This landing page view is what the user sees when they first log in.
    Depending on whether the user is logged in or not, they may see a
    different template.
    """

    return render(request, 'landing_page.html', {
    },
    )


"""
The following views are simple, static pages.
"""

def about(request):
    return render(request, 'about.html', {
    },
    )

def contact(request):
    return render(request, 'contact.html', {
    },
    )

def terms(request):
    return render(request, 'terms.html', {
    },
    )

def privacy(request):
    return render(request, 'privacy.html', {
    },
    )





@login_required
def community(request):
    users = UserProfile.objects.all()
    groups = WorkoutGroup.objects.all()
    tags = Tag.objects.all()
    return render(request, 'community.html', {
        'users' : users,
        'groups' : groups,
        'tags' : tags,
    },
    )


# This is for forgot password? section on the login page.
# This page will take in username and email information from the user
# And if the username and email belong to the same user, a password reset
# email will be sent.
def forgot(request):

    #If the request input any information. 
    if (request.method == 'POST'):
        #Create an object of ForgotPasswordForm from the user input.
        forgot_password_form = ForgotPasswordForm(request.POST)

        if forgot_password_form.is_valid():
            #forgot_password_form.save(commit=False)

            #These are the username and email that the user put in. 
            inp_username = forgot_password_form.cleaned_data.get('username')
            inp_email = forgot_password_form.cleaned_data.get('email')
            
            #If the input username is valid, email them the link.
            try:
                user = User.objects.get(username=inp_username)
                if inp_email == user.email:
                    #send_mail('Reset Password', 'Reset Password link', settings.EMAIL_HOST_USER, [user.email])
                    """
                    user.password_reset(request, 
                        template_name='password_reset_form.html', 
                        email_template_name='password_reset_email.html')
                    """
                    return render(request, 'email_sent.html')
            except User.DoesNotExist:
                pass 
            return render(request, 'email_not_sent.html')
    else: 
        forgot_password_form = ForgotPasswordForm()

    #Otherwise, stay on that page with the incompelete form. 
    return render(request, 'forgot.html', {'forgot_password_form': forgot_password_form},)
    
    
"""
#Reset password upon request.  
def reset_pw(request):
    if (request.method == 'POST'):
        #Create an object of ResetPasswordForm from the user input.
        reset_pw_form = PasswordResetForm(request.POST)
        if reset_pw_form.is_valid():
            pass
"""
