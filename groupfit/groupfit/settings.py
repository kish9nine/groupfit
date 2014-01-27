###############################################################################

"""
Django settings for groupfit project.

General application settings.
"""

import os
import secret

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
SECRET_KEY = secret.SECRET_KEY

ROOT_URLCONF = 'groupfit.urls'

WSGI_APPLICATION = 'groupfit.wsgi.application'

###############################################################################

"""
Database settings for connecting to the MySQL database.
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': secret.DB_NAME,
        'USER': secret.DB_USER,
        'PASSWORD': secret.DB_PASSWORD,
        'HOST': secret.DB_HOST,
        'PORT': '',
    }
}

###############################################################################

"""
Django project configurations.
"""

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.core.mail',
    'groupfit',
    'users',
    'groups',
    'tags',
    'playlists',
    'django_gravatar',
    'south',
    'easy_thumbnails',
    'social_auth'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/')
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

###############################################################################

"""
Authentication settings.
"""

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

FACEBOOK_APP_ID = secret.FACEBOOK_APP_ID
FACEBOOK_API_SECRET = secret.FACEBOOK_API_SECRET
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

GOOGLE_CONSUMER_KEY          = secret.GOOGLE_CONSUMER_KEY
GOOGLE_CONSUMER_SECRET       = secret.GOOGLE_CONSUMER_SECRET
GOOGLE_OAUTH2_CLIENT_ID      = secret.GOOGLE_OAUTH2_CLIENT_ID
GOOGLE_OAUTH2_CLIENT_SECRET  = secret.GOOGLE_OAUTH2_CLIENT_SECRET

###############################################################################

"""
Language / Internationalization settings.
"""

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = (
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)

###############################################################################

###############################################################################

"""
Thumbnail alias configuration for easy_thumbnails.
"""

THUMBNAIL_ALIASES = {
    '': {
        'gravatar-full': {'size': (512, 512), 'crop': True},
    },
}

###############################################################################

"""
Static file configuration.
"""

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

###############################################################################

"""
Simple logging configuration.
"""

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



"""
Social Auth Login
"""
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UUID_LENGTH = 16
#SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]

###############################################################################

"""
EasyMap settings, specfically default map center.
"""

#EASY_MAPS_CENTER = (42.361138,-71.092374)

###############################################################################

"""
Email configuration settings.
"""

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


EMAIL_HOST_USER = secret.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = secret.EMAIL_HOST_PASSWORD


##############################################################################

