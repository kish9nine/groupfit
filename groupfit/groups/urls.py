from django.conf.urls import patterns, include, url
from groups.views import view_group, create_group, leave_group, join_group

urlpatterns = patterns('',

    url(r'^create/$', create_group),            # matches /groups/create
    url(r'^join/(?P<group_pk>\d+)$', join_group), # matches /groups/leave/<pk>
    url(r'^leave/(?P<group_pk>\d+)$', leave_group), # matches /groups/leave/<pk>
    url(r'^(?P<group_pk>\d+)$', view_group),    # matches /groups/<pk>

)
