django-project-template
=======================

At [Blimp](http://getblimp.com/), we love working with Django. For every project we start we always ended up doing the same thing. Installing Django, setting up environment settings, installing South, etc... So I decided to take all of that and create a Django Project Template to use with the startproject command new in Django 1.4. This template has a couple of useful settings and Fabric commands that make deploying, managing, and using Django with Heroku easier.

#How to install

    django-admin.py startproject --template=https://github.com/jpadilla/django-project-template/archive/1.4.zip --extension=py,md,dev project_name

#Apps included
	Fabric
	South
	dj-database-url
	django-extensions
	gunicorn
	psycopg2

#Settings
The manage.py script checks for an environment variable called `ENVIRONMENT` with values of STAGING or PRODUCTION. If none of those are found, development environment is assumed. We use this to automatically set `DJANGO_SETTINGS_MODULE`. This makes using manage.py easier because you dont have to keep remembering of writing `--setting=project.settings.development`. We converted settings.py into a module with settings splitted into three different files, `development.py`, `staging.py`, `production.py`. All of those import common settings from `common.py` and override them or set new ones depending on the environment.


#Fabric Script

##Environments
	fab development 'command'
	fab staging 'command'
	fab production 'command'

##Deployment
	fab production deploy
	fab production collectstatic
	fab brunchwatch
	fab brunchbuild

##DB
	fab staging resetdb
	fab schemamigration
	fab migrate
	fab updatedb

##Heroku
	fab production ps
	fab production restart
	fab production tail
	fab production shell
	fab production config

