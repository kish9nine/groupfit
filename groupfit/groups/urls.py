from django.conf.urls import patterns, include, url
from groups.views import view_group, create_group

urlpatterns = patterns('',

    url(r'^create/$', create_group),            # matches /groups/create
    url(r'^(?P<group_pk>\d+)$', view_group),    # matches /groups/<pk>

)
