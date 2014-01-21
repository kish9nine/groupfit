from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from groupfit.views import home, about, contact, terms, privacy
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',

    # Website default pages.
    url(r'^$', home),
    url(r'^about$', about),
    url(r'^contact$', contact),
    url(r'^terms$', terms),
    url(r'^privacy$', privacy),

    # User accounts app pages.
    url(r'^user/', include('users.urls')),

    # Group app pages.
    url(r'^group/', include('groups.urls')),

    # Tags app pages.
    url(r'tag/', include('tags.urls')),

    # Administrator view.
    url(r'^admin/', include(admin.site.urls)),

    # Authentication urls.
    url(r'^login$', login, {'template_name': 'login.html'}),
    url(r'^logout$', logout, {'next_page': '/'}),
)
