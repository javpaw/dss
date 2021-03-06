# Django settings for dss project.
import sys
import os
import djcelery
djcelery.setup_loader()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

#path al root del proyecto
PROJECT_ROOT = os.path.dirname (
            os.path.dirname(
              os.path.abspath(__file__)
            )
          )


MANAGERS = ADMINS

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
       'NAME': 'dss',                      # Or path to database file if using sqlite3.
       'USER': 'dss',                      # Not used with sqlite3.
       'PASSWORD': 'dss',                  # Not used with sqlite3.
       'HOST': '10.10.10.67',                      # Set to empty string for localhost. Not used with sqlite3.
       'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
   }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
PROJECT_PATH = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2])

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
# STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1]+['_res']),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'phcn)d69gvhi43q7*3+kki9z9yr2(zt+5!nnf5bxzs5sjt0s=%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dss.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'dss.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1]+['templates']),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'south',
    'sensors',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'djcelery',
    'djcelery.transport',
)
BROKER_URL = 'django://'


BROKER_BACKEND = 'django'

# REDIS_DB = 0
# REDIS_CONNECT_RETRY = True
# CELERY_RESULT_BACKEND = 'redis'
# CELERY_REDIS_PORT = 9333
# CELERY_REDIS_PASSWORD = '7109efd5f43b84b2cd05c645b1d52ad8'
# CELERY_REDIS_HOST = 'koi.redistogo.com'
# BROKER_URL = os.getenv('REDISTOGO_URL', 'redis://julianamaya:7109efd5f43b84b2cd05c645b1d52ad8@koi.redistogo.com:933')
# BROKER_TRANSPORT = 'redis'
# BROKER_BACKEND = 'redis'
# BROKER_PORT = CELERY_REDIS_PORT
# BROKER_HOST = CELERY_REDIS_HOST
# BROKER_VHOST = '/'
# BROKER_PASSWORD = CELERY_REDIS_PASSWORD
# CELERYD_CONCURRENCY = 1
# CELERY_RESULT_PORT = 9104
# CELERY_TASK_RESULT_EXPIRES = 60 * 10
# import os
if [(i,k) for i,k in os.environ.items() if 'heroku' in k]: #detect heroku somehow reliably

    CACHES = {
        'default': {
            'BACKEND': 'django_pylibmc.memcached.PyLibMCCache'
        }
    }
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(default='postgres://dss:dss@10.10.10.67/dss')}
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '10.10.10.67:11211',
            'TIMEOUT': 3000,
        }
    }
    DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
           'NAME': 'dss',                      # Or path to database file if using sqlite3.
           'USER': 'dss',                      # Not used with sqlite3.
           'PASSWORD': 'dss',                  # Not used with sqlite3.
           'HOST': '10.10.10.67',                      # Set to empty string for localhost. Not used with sqlite3.
           'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
           'TIMEOUT': 3000,
       }
}
# BROKER_URL = 'django://'

# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'


#################################################################
#Configure Database for test
#################################################################

if 'test' in sys.argv:
    try:
        from test_settings import *
    except:
        pass



