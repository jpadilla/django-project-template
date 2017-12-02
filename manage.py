#!/usr/bin/env python
import os
import sys

import dotenv


dotenv.read_dotenv()


if __name__ == '__main__':
    ENVIRONMENT = os.getenv('ENVIRONMENT')

    if ENVIRONMENT == 'STAGING':
        settings = 'staging'
    elif ENVIRONMENT == 'PRODUCTION':
        settings = 'production'
    else:
        settings = 'development'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.setting')
    os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

    try:
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Couldn\'t import Django. Are you sure it\'s installed and '
            'available on your PYTHONPATH environment variable? Did you '
            'forget to activate a virtual environment?'
        ) from exc
    execute_from_command_line(sys.argv)
