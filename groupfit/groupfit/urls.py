from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from groupfit.views import landing_page, about, contact, terms, privacy, forgot #reset_pw
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
    
    ## Forgot password?
    url(r'^forgot/$', forgot),
    
    ## Reset password
    #url(r'^password_reset/$', reset_pw),
    
    ## Register shortcut
    #url(r'^register/$', create_user),

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
