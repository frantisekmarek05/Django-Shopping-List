"""
Django Settings Module for Shopping List Project

This module contains all Django settings for the Shopping List application.
It includes configurations for:
- Security settings (DEBUG, SECRET_KEY, etc.)
- Application dependencies
- Database configuration
- Authentication settings
- Static and media file handling
- Internationalization
- Custom application settings

For more information on Django settings, see:
https://docs.djangoproject.com/en/stable/topics/settings/
"""

# import django_heroku

import os

# Security Settings
# SECURITY WARNING: keep this secret in production!
SECRET_KEY = 'django-insecure-!$x&1m2_tvojeklic1234567890abcdefghijklmno'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# List of all Django apps used in the project
INSTALLED_APPS = [
    'django.contrib.admin',          # Django admin interface
    'django.contrib.auth',           # Authentication system
    'django.contrib.contenttypes',   # Framework for content types
    'django.contrib.sessions',       # Session framework
    'django.contrib.messages',       # Messaging framework
    'django.contrib.staticfiles',    # Static files management
    'shopping_list',                 # Main shopping list application
]

# Middleware configuration
# List of middleware classes for request/response processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',         # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session support
    'django.middleware.common.CommonMiddleware',            # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',            # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Messages support
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static file serving
]

# Root URL Configuration
ROOT_URLCONF = 'shopping_project.urls'

# Template Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Global templates directory
        'APP_DIRS': True,  # Look for templates in app directories
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

# WSGI Configuration
WSGI_APPLICATION = 'shopping_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

# Password Validation
# Password validation rules for user authentication
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# Internationalization Configuration
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True  # Internationalization

USE_L10N = True  # Localization

USE_TZ = True    # Timezone support


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Static Files Configuration (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication settings
LOGIN_URL = 'login'                  # URL for login page
LOGIN_REDIRECT_URL = 'index'         # Redirect after login
LOGOUT_REDIRECT_URL = 'login'        # Redirect after logout

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'shopping_list': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

#django_heroku.settings(locals())