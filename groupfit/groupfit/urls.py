from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from groupfit.views import home, about, contact, terms

urlpatterns = patterns('',

    # Website default pages.
    url(r'^$', home),
    url(r'^about/$', about),
    url(r'^contact$', contact),
    url(r'^terms$', terms),

    # User accounts app pages.
    url(r'^user/', include('users.urls')),

    # Administrator view.
    url(r'^admin/', include(admin.site.urls)),

)
