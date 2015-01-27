#!/usr/bin/env python
import os
import sys

import dotenv


dotenv.read_dotenv()


if __name__ == "__main__":
    ENVIRONMENT = os.getenv('ENVIRONMENT')

    if ENVIRONMENT == 'STAGING':
        settings = 'staging'
    elif ENVIRONMENT == 'PRODUCTION':
        settings = 'production'
    else:
        settings = 'development'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
