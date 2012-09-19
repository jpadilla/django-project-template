import os

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'STAGING':
    from staging import *
elif ENVIRONMENT == 'PRODUCTION':
    from production import *