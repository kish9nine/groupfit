from django.conf.urls import patterns, include, url
from users.views import home

urlpatterns = patterns('',

    # User homepage.
    url(r'^$', home),

)
