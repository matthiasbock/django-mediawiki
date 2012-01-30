# Django settings for banking project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('webmaster', 'webmaster@localhost'),
)

MANAGERS = ADMINS

DATABASE = {
	'wiki': {
		'ENGINE':	'django.db.backends.mysql',
		'NAME':		'wiki',
		'USER': 	'Django',
		'PASSWORD':	'',
		'HOST':		'',
		'PORT':		'',
		}
	}
DATABASES = { 'default': DATABASE['wiki'] }

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'de-DE'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.middleware.csrf.CsrfResponseMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
)

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

ROOT_URLCONF = 'Django.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	"/var/www/Django/mediawiki/templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

