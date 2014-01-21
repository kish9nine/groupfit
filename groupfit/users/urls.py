from django.conf.urls import patterns, include, url
from users.views import view_user

urlpatterns = patterns('',

    # View a user profile.
    url(r'^(?P<user_pk>\d+)$', view_user),

)
