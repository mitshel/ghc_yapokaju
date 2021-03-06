"""
Django settings for yapokazhu project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g6qtgbcvn=yuep2_&(5_sj8wi#3^e@y+-&6)c$t-ecq(%*_%f0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pyhammer.beget.tech', '.xn--80amkpe2a2f.xn--p1ai']

INTERNAL_IPS = ['127.0.0.1', ]


# Application definition

INSTALLED_APPS = [
    'appconf',
    'betterforms',
    'debug_toolbar',
    'django_filters',
    'extra_views',
    'formtools',
    'registration',
    'sorl.thumbnail',
    'widget_tweaks',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'apps.account',
    'apps.clndr',
    'apps.core'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


AUTH_USER_MODEL = 'account.User'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('ru', _('Russian')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#STATIC_DIR = 'static'

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

STATICFILES_DIRS = [
    'assets',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATIC_URL = '/static/'
#STATIC_ROOT =  os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/media/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')


# https://docs.djangoproject.com/en/2.1/topics/email/#smtp-backend

EMAIL_HOST = "smtp.beget.com"
EMAIL_HOST_USER = "no-reply@yapokaju.ru"
EMAIL_HOST_PASSWORD = "xxxxxx"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
SERVER_EMAIL = "no-reply@yapokaju.ru"
DEFAULT_FROM_EMAIL = "no-reply@yapokaju.ru"


ACCOUNT_ACTIVATION_DAYS = 3

REGISTRATION_FORM = 'apps.account.forms.RegistrationForm'
LOGOUT_REDIRECT_URL = '/'

MAX_SUBSCRIPTIONS = 2
