"""
Django settings for FeedbuzzClient project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+1_k-evizgfw_$0rbp3*ep7k4%hvn!^mo0hm4^vi@_y2p_)p52'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','FeedBuzzDemo.pythonanywhere.com']

TIMEOUT = 3600
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feedpanel.apps.FeedpanelConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FeedbuzzClient.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'FeedbuzzClient.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
MEDIA_URL="/media/"



##################### The Below Code is used in LOCALHOST #####################
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'OPTIONS': {
                    'charset': 'utf8mb4',
                    'use_unicode': True, },
        'NAME': 'feedbuzzanalytics',
        'USER': 'root',
        'PASSWORD':"",    
        'HOST': "localhost",
        'PORT':'3306'    
    }
}
STATIC_ROOT = os.path.join(BASE_DIR,'assets')
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
###############################################################################


##################### The Below Code is used in CLOUD #########################

# DATABASES = {
#     'default': {
        
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'FeedBuzzDemoAdmi$feedbuzzanalytics',
#           'OPTIONS': {
#                     'charset': 'utf8mb4',
#                     'use_unicode': True, },
#         'USER': 'FeedBuzzDemoAdmi',
#         'PASSWORD':"Test@1999",    
#         'HOST': "FeedBuzzDemoAdmin.mysql.pythonanywhere-services.com",
#     }
# }

# STATIC_ROOT = '/home/FeedBuzzDemo/FeedbuzzClient/assets/'
# MEDIA_ROOT="/home/FeedBuzzDemo/FeedbuzzClient/media"

###############################################################################

