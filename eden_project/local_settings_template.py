# Fill in the database connection information below.
# STATFILEDIR may need to be filled in depending on how you set up your server.
# Change the filename to 'local_settings.py'
# Request the SECRET_KEY from CIDA staff.
# You should be good to go.
# Never commit any files containing sensitive information to source control.

import os.path
import secure
import secret_key

PROJECT_HOME = os.path.dirname(__file__)
SITE_HOME = os.path.join(PROJECT_HOME, "..")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': secure.DB_SCHEMA,  # Or path to database file if using sqlite3.
        'USER': secure.DB_USER,  # Not used with sqlite3.
        'PASSWORD': secure.DB_PASSWORD,  # Not used with sqlite3.
        'HOST': secure.DB_HOST,  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

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
# STATIC_ROOT = '/var/www/static/'
STATIC_ROOT = os.path.expanduser("~/public_html/static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# If you omit the protocol and host, they will be derived from the page's URL.
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = ()

# Option -- should Dygraph range selection be by an overview graph (True), or by
# gestures within the main graph (False)?
DYGRAPH_RANGE_SELECTOR = True


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# work directory for Matplotlib -- must be writable by web service process
MATPLOTLIB_WORK_DIR = "/tmp/matplotlib"

# Make this unique, and don't share it with anybody.
SECRET_KEY = secret_key.SECRET_KEY

