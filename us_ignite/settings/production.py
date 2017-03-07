# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.
from us_ignite.settings.settings import *
import dj_database_url
import urlparse


DEBUG = True

env = os.getenv
# Make these unique, and don't share it with anybody.
SECRET_KEY = env('SECRET_KEY')
NEVERCACHE_KEY = env('NEVERCACHE_KEY')

SITE_URL = "https://us-ignite-v2.herokuapp.com"

########################
# DEPLOY SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['us-ignite-v2.herokuapp.com',
                 'us-ignite.org',
                 'www.us-ignite.org', ]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1


#############
# DATABASES #
#############

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}


#########
# PATHS #
#########

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP

STATICFILES_DIRS = (
    here('assets'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

STATIC_FILES_VERSION = 'v2'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     here('us_ignite/static/mezzanine/'),
#     os.path.join(BASE_DIR, "static"),
#     'us_ignite/static/',
# )

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"

DEFAULT_FILE_STORAGE = 'us_ignite.common.storage.MediaS3Storage'

MEDIA_URL = "/media/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = "%s.urls" % PROJECT_APP

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_BUCKET_NAME')

# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME

AWS_HEADERS = {
                     'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                     'Cache-Control': 'max-age=94608000',
                     }

# Used to make sure that only changed files are uploaded with collectstatic
AWS_PRELOAD_METADATA = True

#http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html
# allows authenticating with creds in querystring for temp access to a resource
# Setting to False if not needed helps get rid of uwanted qstrings in compressed
# output
AWS_QUERYSTRING_AUTH = False
# GEOPOSITION_GOOGLE_MAPS_API_KEY = ''


# Media storage
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# MEDIA_URL = "https://%s/%s/" % (CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)
MEDIA_ROOT = ''
DEFAULT_FILE_STORAGE = 'us_ignite.common.custom_storages.MediaStorage'

THUMBNAIL_DEBUG = False
redis_url = urlparse.urlparse(env('REDISTOGO_URL'))

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': redis_url.password,
        }
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Twitter API:
TWITTER_API_KEY = env('TWITTER_API_KEY')
TWITTER_API_SECRET = env('TWITTER_API_SECRET')

MAILCHIMP_API_KEY = env('MAILCHIMP_API_KEY')
MAILCHIMP_LIST = env('MAILCHIMP_LIST')

MAILCHIMP_GCTC_API_KEY = env('MAILCHIMP_GCTC_API_KEY')
MAILCHIMP_GCTC_LIST = env('MAILCHIMP_GCTC_LIST')

MAILCHIMP_AWT_LIST = env('MAILCHIMP_AWT_LIST')

MAILCHIMP_AWT_POTENTIAL_PROPOSER_LIST = env('MAILCHIMP_AWT_POTENTIAL_PROPOSER_LIST')
MAILCHIMP_AWT_COMPANY_LIST = env('MAILCHIMP_AWT_COMPANY_LIST')
MAILCHIMP_AWT_INTERESTED_OBSERVERS_LIST = env('MAILCHIMP_AWT_INTERESTED_OBSERVERS_LIST')

MAILCHIMP_PAWR_LIST = env('MAILCHIMP_PAWR_LIST')

MAILCHIMP_SGC_LIST = env('MAILCHIMP_SGC_LIST')

# Asset compressor:
# COMPRESS_ENABLED = True
# Heroku does not have a filesystem, used to deploy the assets to S3:
# COMPRESS_STORAGE = 'us_ignite.common.storage.CachedS3BotoStorage'