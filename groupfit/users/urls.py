from django.conf.urls import patterns, include, url
from users.views import view_user, create_user, complete_goal

urlpatterns = patterns('',
    # Create a user profile.
    url(r'^create/$', create_user),

    # Mark a goal as completed.
    url(r'^complete/(?P<goal_pk>\d+)$', complete_goal),

    # View a user profile.
    url(r'^(?P<user_pk>\d+)$', view_user),

)
