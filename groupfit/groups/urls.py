from django.conf.urls import patterns, include, url
from groups.views import view_group

urlpatterns = patterns('',

    url(r'^(?P<group_pk>\d+)$', view_group),

)
