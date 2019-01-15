# Django 2.0+ project template

This is a simple Django 2.0+ project template with my preferred setup. Most Django project templates make way too many assumptions or are just way too complicated. I try to make the least amount of assumptions possible while still trying provide a useful setup. Most of my projects are deployed to Heroku, so this is optimized for that but is not necessary.

## Features

- Django 2.0+
- Uses [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from Python.org.
- [Django](https://www.djangoproject.com/) 2.0+
- Based on [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.
- Externalized logging configuration based on [Good logging practice in Python](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/)

## How to install

```bash
mkdir project_name
cd project_name
pipenv --python <version>
pipenv install django
pipenv run django-admin.py startproject \
  --template=https://github.com/jpadilla/django-project-template/archive/master.zip \
  --name=Procfile \
  --extension=py,md,env,json \
  project_name .
pipenv install -r requirements/common.txt
pipenv install -r requirements/dev.txt --dev
rm -rf requirements
cp example.env .env
cp example.logging.json logging.json
```

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```dotenv
ENVIRONMENT=DEVELOPMENT
DJANGO_SECRET_KEY=dont-tell-eve
DJANGO_DEBUG=yes
...
```

These settings(and their default values) are only used on staging and production environments.

```dotenv
DJANGO_SESSION_COOKIE_SECURE=yes
DJANGO_SECURE_BROWSER_XSS_FILTER=yes
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF=yes
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=yes
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=
DJANGO_SECURE_SSL_HOST=
DJANGO_SECURE_SSL_REDIRECT=yes
DJANGO_SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https
```

## Deployment

It is possible to deploy to Heroku or to your own server.

### Heroku

```bash
$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`
heroku create
heroku addons:add heroku-postgresql:hobby-dev
heroku pg:promote DATABASE_URL
heroku config:set ENVIRONMENT=PRODUCTION
heroku config:set DJANGO_ALLOWED_HOSTS='[app-name].herokuapp.com'
heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`
git push heroku master
heroku run python manage.py createsuperuser
```

## License

The MIT License (MIT)

Copyright (c) 2012-2017 José Padilla

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
