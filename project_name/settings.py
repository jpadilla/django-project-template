"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""
import os

from configurations import Configuration, values


class Common(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)

    ALLOWED_HOSTS = []

    # Application definition
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'django_extensions',
    )

    MIDDLEWARE_CLASSES = (
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = '{{ project_name }}.urls'

    WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )

    # Internationalization
    # https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
    STATIC_URL = '/static/'


class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []

    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'debug_toolbar',
    )


class Staging(Common):
    """
    The in-staging settings.
    """
    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'djangosecure',
    )

    # django-secure
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_PROXY_SSL_HEADER = values.TupleValue(
        ('HTTP_X_FORWARDED_PROTO', 'https')
    )


class Production(Staging):
    """
    The in-production settings.
    """
    pass
