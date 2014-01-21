from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'landing_page.html', {
    },
    )

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
