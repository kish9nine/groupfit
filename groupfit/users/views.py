from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import UserProfile, create_user_profile

def create_user(request):
    #If the user is trying to add info to the server,
    if request.method == 'POST':
        #Feed as arguments to RegisterForm the inputs from the user.
        create_user_form = RegisterForm(request.POST)
        #If username and password are of the right length and email is of the valid form,
        #And password and confirm password identical, 
        if create_user_form.is_valid():
            #Don't save the user in creation as a new user yet. 
            new_user = create_user_form.save(commit=False)
            
            #Then create UserProfile object from 
            new_userProfile = create_user_profile(new_user)
            
            #Render a Welcome to GroupFit page if the input info is valid. 
            return redirect('users.views.welcome', new_user.username)
            
            #Send an email as well. 
            
            
    else:
        #If the user didn't plug in anything, create_user_form will be an empty shell?
        create_user_form = RegisterForm()
    return render(request, 'create_user.html', {})
        
        

@login_required
def view_user(request, user_pk=-1):
    if user_pk == -1:
        user_pk = request.user.userprofile.pk
    user = get_object_or_404( UserProfile, pk=user_pk )
    return render(request, 'view_user.html', {
        'profile': user,
    },
    )

