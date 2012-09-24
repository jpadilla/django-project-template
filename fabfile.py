from fabric.api import *

# current_git_branch = local('git symbolic-ref HEAD', capture=True).split('/')[-1]


# === Environments ===
def development():
    env.env = 'development'
    env.settings = '{{ project_name }}.settings.development'


def staging():
    env.env = 'staging'
    env.settings = '{{ project_name }}.settings.staging'
    env.remote = ''
    env.heroku_app = ''


def production():
    env.env = 'production'
    env.settings = '{{ project_name }}.settings.production'
    env.remote = ''
    env.heroku_app = ''


# Default Environment
development()


# === Deployment ===
def deploy():
    local('git push {remote}'.format(**env))


# === Static assets stuff ===
def collectstatic():
    # brunchbuild()
    local('python manage.py collectstatic --noinput -i app -i config.coffee \
            -i node_modules -i package.json --settings={settings}'.format(**env))
    # if env.env != 'development':
    #     commit_id = local('git rev-parse HEAD', capture=True)
    #     _config_set(key='HEAD_COMMIT_ID', value=commit_id)


def brunchwatch(app_name='core'):
    local('cd {{ project_name }}/%s/static/ && brunch w' % app_name)


def brunchbuild(app_name='core'):
    with settings(warn_only=True):
        local('rm -r {{ project_name }}/%s/static/public/' % app_name)
    local('cd {{ project_name }}/%s/static/ && brunch b -m' % app_name)


# === DB ===
def resetdb():
    if env.env == 'development':
        with settings(warn_only=True):
            local('rm dev.sqlite3')
        local('python manage.py syncdb --settings={settings}'.format(**env))
        local('python manage.py migrate --settings={settings}'.format(**env))
    else:

        if raw_input('\nDo you really want to RESET DATABASE of {heroku_app}? YES or [NO]: '.format(**env)) == 'YES':
            local('heroku run python manage.py syncdb --noinput --settings={settings} --app {heroku_app}'.format(**env))
            local('heroku run python manage.py migrate --settings={settings} --app {heroku_app}'.format(**env))
        else:
            print '\nRESET DATABASE aborted'


def schemamigration(app_names='core'):
    local('python manage.py schemamigration {app_names} --auto --settings={settings}'.format(app_names, **env))


def migrate():
    if env.env == 'development':
        local('python manage.py migrate --settings={settings}'.format(**env))
    else:

        if raw_input('\nDo you really want to MIGRATE DATABASE of {heroku_app}? YES or [NO]: '.format(**env)) == 'YES':
            local('heroku run python manage.py migrate --settings={settings} --app {heroku_app}'.format(**env))
        else:
            print '\nMIGRATE DATABASE aborted'


def updatedb():
    schemamigration()
    migrate()


# === Heroku ===
def ps():
    local('heroku ps --app {heroku_app}'.format(**env))


def restart():
    if raw_input('\nDo you really want to RESTART (web/worker) {heroku_app}? YES or [NO]: '.format(**env)) == 'YES':
        local('heroku ps:restart web --app {heroku_app}'.format(**env))
    else:
        print '\nRESTART aborted'


def tail():
    local('heroku logs --tail --app {heroku_app}'.format(**env))


def shell():
    local('heroku run bash --app {heroku_app}'.format(**env))


def config():
    local('heroku config --app {heroku_app}'.format(**env))


def _config_set(key=None, value=None):
    if key and value:
        local('heroku config:set {}={} --app {heroku_app}'.format(key, value, **env))
    else:
        print '\nErr!'
