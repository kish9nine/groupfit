from django.conf.urls import patterns, include, url
from users.views import view_user, create_user, create_user_goal

urlpatterns = patterns('',
    # Create a user profile.
    url(r'^create/$', create_user),

    # Create a user goal
    url(r'^create/goal$', create_user_goal),

    # View a user profile.
    url(r'^(?P<user_pk>\d+)$', view_user),

)
