"""
ASGI config for {{ project_name }} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/asgi/
"""

import os


configuration = os.getenv('ENVIRONMENT', 'development').title()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', configuration)

from configurations import importer  # noqa
importer.install()

from django.core.asgi import get_asgi_application   # noqa
application = get_asgi_application()
