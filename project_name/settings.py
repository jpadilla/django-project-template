"""
For the full list of settings and their values,
see https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
from typing import Optional

import sentry_sdk
from configurations import Configuration, values
from sentry_sdk.integrations.django import DjangoIntegration


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = values.SecretValue()
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = [
        '*',
    ]

    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    # Application definition
    INSTALLED_APPS = [
        'whitenoise.runserver_nostatic',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'apps.core',
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

    ROOT_URLCONF = '{{ project_name }}.urls'

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

    WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

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
    # See http://whitenoise.evans.io/en/stable/
    STATIC_URL = '/static/'

    # SESSION_COOKIE_SECURE = False
    # SECURE_BROWSER_XSS_FILTER = False
    # SECURE_CONTENT_TYPE_NOSNIFF = False
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    # SECURE_HSTS_SECONDS = 86400
    # SECURE_REDIRECT_EXEMPT = []
    # SECURE_SSL_HOST = None
    # SECURE_SSL_REDIRECT = False
    # SECURE_PROXY_SSL_HEADER = (
    #     ('HTTP_X_FORWARDED_PROTO', 'https'),
    # )

    # rest framework
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
            'rest_framework.renderers.JSONRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'djangorestframework_camel_case.parser.CamelCaseJSONParser',
            'rest_framework.parsers.JSONParser',
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 100,
    }

    # Sentry
    SENTRY_DSN: Optional[str] = values.URLValue(environ_prefix=None, default=None)
    if SENTRY_DSN:
        sentry_sdk.init(
            dsn=SENTRY_DSN,
            integrations=[DjangoIntegration()],
        )

    # Database
    DATABASES = values.DatabaseURLValue()

    # Cache
    CACHES = values.CacheURLValue()


class Dev(Common):
    DEBUG = True
