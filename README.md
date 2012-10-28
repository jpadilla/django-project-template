django-project-template
=======================

Django 1.4+ project template layout.

    django-admin.py startproject --template=https://github.com/jpadilla/django-project-template/zipball/master --extension=py,md,dev project_name
    
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
	
