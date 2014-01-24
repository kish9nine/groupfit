from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from forms import ForgotPasswordForm  #This is where forgot password? form is.
from django.core.exceptions import ObjectDoesNotExist #I don't need it while I am using User.DoesNotExist instead

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
        #Create an object of ForgotPasswordForm from the user input.
        forgot_password_form = ForgotPasswordForm(request.POST)
        
        if forgot_password_form.is_valid():
            forgot_password_form.save(commit=False)
            
            #These are the username and email that the user put in. 
            inp_username = forgot_password_form.fields['username']
            inp_email = forgot_password_form.fields['email']
        
            #If the input username is in User database and email corresponds to that username return email_sent page.
            if User.objects.get(username=inp_username) is not User.DoesNotExist:
                if User.objects.get(username=inp_username).email == inp_email:
                    #send_email('Reset Password', 'Reset Password link', 'admin@groupfit.rouly.net', inp_email)
                    return render(request, 'email_sent.html') #It might be nice if we could turn this into a pop-up instead.
                return render(request, 'email_not_sent.html')
    else: 
        forgot_password_form = ForgotPasswordForm(request.POST)
    
    #Otherwise, stay on that page with the incompelete form. 
    return render(request, 'forgot.html', {'forgot_password_form': forgot_password_form},)
    
    
    
    
