from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from groupfit.views import landing_page, about, contact, terms
from groupfit.views import privacy, forgot, community
from django.contrib.auth.views import login, logout
from users.views import view_user, create_user

urlpatterns = patterns('',

    # Website default pages.
    url(r'^$', landing_page),   # matches /
    url(r'^about$', about),     # matches /about
    url(r'^contact$', contact), # matches /contact
    url(r'^terms$', terms),     # matches /terms
    url(r'^privacy$', privacy), # matches /privacy

    # User accounts app pages.
    url(r'^me$', view_user),                     # matches /me
    url(r'^user/', include('users.urls')),       # matches /user/...

    # Community page.
    url(r'community$', community),

    ## Forgot password?
    url(r'^forgot$', forgot, name = 'forgot'),

    ## Register shortcut
    url(r'^register$', create_user, name = 'register'),
    ## Register or login using Facebook, Twitter, or Google Account.
    url(r'', include('social_auth.urls')),

    # Group app pages.
    url(r'^group/', include('groups.urls')),    # matches /group/...

    # Tags app pages.
    url(r'tag/', include('tags.urls')),         # matches /tag/...

    # Playlist app pages.
    url(r'^playlist/', include('playlists.urls')), # matches /playlist/...

    # Administrator view.
    url(r'^admin/', include(admin.site.urls)),

    # Authentication urls.
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, {'next_page': '/'}),


    

)
