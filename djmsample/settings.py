"""
Django settings for the Djmongo Sample project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


import os
from django.contrib.messages import constants as messages
from .utils import bool_env
import dj_database_url
from getenv import env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_DIR = os.path.join(BASE_DIR, 'db')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'SECRET_KEY', '@+ttixefm9-bu1eknb4k^5dj(f1z0^97b$zan9akdr^4s8cc54')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool_env(env('DEBUG', True))

TEMPLATE_DEBUG = bool_env(env('DEBUG', True))

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Djmongo -----------------------------------------------------
    'djmongo',
    'djmongo.accounts',
    'djmongo.console',
    'djmongo.read',
    'djmongo.dataimport',
    'djmongo.write',
    'djmongo.aggregations',


    # 3rd party
    'corsheaders',
    'bootstrapform',
    'widget_tweaks',
    'django_extensions',
]

MIDDLEWARE = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djmsample.urls'

WSGI_APPLICATION = 'djmsample.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
     },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
     },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.NumericPasswordValidator',
     },
]


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASES_CUSTOM',
                    'sqlite:///{}/db/db.sqlite3'.format(BASE_DIR))
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = str(os.path.join(BASE_DIR, 'collectedstatic'))


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'


# CORS Settings
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = ('GET', 'POST',)
MIDDLEWARE += ('corsheaders.middleware.CorsMiddleware',)


# Djmongo Settings --------------
MONGODB_CLIENT = env("MONGODB_CLIENT", "mongodb://127.0.0.1:27017")
MONGO_LIMIT = int(env("MONGO_LIMIT", "200"))


# Authentication Backends
AUTHENTICATION_BACKENDS = ('djmongo.accounts.auth.HTTPAuthBackend',
                           'django.contrib.auth.backends.ModelBackend',)
# Login URL
LOGIN_REDIRECT_URL = '/djm/accounts/login'
LOGIN_URL = '/djm/accounts/login'

# Pretty Bootstrap3 messages.

MESSAGE_TAGS = {messages.DEBUG: 'debug',
                messages.INFO: 'info',
                messages.SUCCESS: 'success',
                messages.WARNING: 'warning',
                messages.ERROR: 'danger', }
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# Expire in 30 minutes
SESSION_COOKIE_AGE = int(env('SESSION_COOKIE_AGE', int(30 * 60)))

# Expire when browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SAMESITE = None
