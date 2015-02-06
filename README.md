# Django 1.7+ project template

[![Dependency Status](https://gemnasium.com/jpadilla/django-project-template.svg)](https://gemnasium.com/jpadilla/django-project-template)

This is a simple Django 1.7+ project template with my preferred setup. Most Django project templates make way too many asumptions or are just way too complicated. I try to make the least amount of asumptions possible while still trying provide a useful setup. Most of my projects are deployed to Heroku, so this is optimized for that but is not necessary.

**Note**: If you're looking for the previous Django 1.4+ project template layout check out the [1.4](https://github.com/jpadilla/django-project-template/tree/1.4) branch.

## Features

- Django 1.7.1
- Development, Staging and Production settings with [django-configurations](http://django-configurations.readthedocs.org/).
- Get value insight and debug information while on Development with [django-debug-toolbar](http://django-debug-toolbar.readthedocs.org/en/1.2.2/).
- Load environment variables from `.env` with [django-dotenv](https://github.com/jpadilla/django-dotenv).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org/).
- HTTPS and other security related settings on Staging and Production with [django-secure](http://django-secure.readthedocs.org/).
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.

## How to install

```bash
$ django-admin.py startproject --template=https://github.com/jpadilla/django-project-template/archive/master.zip --name=Procfile --extension=py,md,env project_name
$ mv example.env .env
$ pip install -r requirements.txt
```

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'
DJANGO_TEMPLATE_DEBUG='yes'
```

These settings(and their default values) are only used on staging and production environments.

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_FRAME_DENY='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
```

## Deployment

It is possible to deploy to Heroku or to your own server.

### Heroku

```bash
$ heroku create
$ heroku addons:add heroku-postgresql:dev
$ heroku addons:add newrelic
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`
```
