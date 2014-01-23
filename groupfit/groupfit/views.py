from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from forms import ForgotPasswordForm  #This is where forgot password? form is.

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


#This is for forgot password? section on the login page. 
#This page will take in username and email information from the user  
#And if the username and email belong to the same user, a password reset email will be sent. 
def forgot(request):
    
    #If the request input any information.
    if (request.method == 'POST'):
        forgot_password_form = ForgotPasswordForm(request.POST)
        username = forgot_password_form.username
        if username in User.objects.all() and forgot_password_form.pass
    
    return render(request, 'forgot.html', {},)
