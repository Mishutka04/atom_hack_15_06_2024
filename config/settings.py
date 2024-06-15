import os
from pathlib import Path

import environ

# import sentry_sdk
# from sentry_sdk.integrations.celery import CeleryIntegration
# from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# -----------------------------------------------------------------------------------------------
# - BASE ----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

DEBUG = env.bool("DEBUG", default=True)

SECRET_KEY = env("SECRET_KEY", default="!!! SET SECRET KEY !!!")

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=["localhost", "127.0.0.1", "localhost:3000"]
    )

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'drfpasswordless',

    # -------------------------------------------------------------------------
    # - PROJECT APPS ----------------------------------------------------------
    # -------------------------------------------------------------------------
    'users',
    'support',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# -----------------------------------------------------------------------------------------------
# - AUTHENTICATION ------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.User'

PASSWORDLESS_AUTH = {
   'PASSWORDLESS_AUTH_TYPES': ['EMAIL'],
   'PASSWORDLESS_EMAIL_NOREPLY_ADDRESS': 'noreply@example.com',
}
# -----------------------------------------------------------------------------------------------
# - DJANGO REST FRAMEWORK -----------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

REST_FRAMEWORK = {

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # 'DEFAULT_FILTER_BACKENDS': [
    #     'django_filters.rest_framework.DjangoFilterBackend',
    # ],
    # 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# -----------------------------------------------------------------------------------------------
# - INTERNATIONALIZATION ------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# -----------------------------------------------------------------------------------------------
# - STATIC FILES --------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'dist/static/')

MEDIA_URL = "/uploads/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# -----------------------------------------------------------------------------------------------
# - DATABASES -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 180,  # in seconds
            # see also
            # https://docs.python.org/3.7/library/sqlite3.html#sqlite3.connect
        }
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------------------------------------------------------------
# - SECURITY ------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

if DEBUG is True:
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:3000',
        'http://127.0.0.1:5500',
        'http://localhost:5173',
    )
    
# -----------------------------------------------------------------------------
# - EMAIL ---------------------------------------------------------------------
# -----------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_HOST = 'smtp.mail.ru'
# EMAIL_PORT = 465
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

# -----------------------------------------------------------------------------
# - TRANSFORMERS --------------------------------------------------------------
# -----------------------------------------------------------------------------

TOKEN_TRANSFORMRS_API = env("TOKEN_TRANSFORMRS_API", default="")
