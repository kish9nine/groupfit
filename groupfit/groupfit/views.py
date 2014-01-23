from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
def forgot(request):
    return render(request, 'forgot.html', {},)
