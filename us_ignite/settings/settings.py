from __future__ import absolute_import, unicode_literals
import os

from django import VERSION as DJANGO_VERSION
from django.utils.translation import ugettext_lazy as _


# Full filesystem path to the project.
PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = 'us_ignite'
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

here = lambda *x: os.path.join(PROJECT_ROOT, '..', *x)


########################
# DEPLOY SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['us-ignite-staging.herokuapp.com',
                 'us-ignite.org',
                 'www.us-ignite.org', ]


######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for conveniently
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
ADMIN_MENU_ORDER = (
    ("Content", ("pages.Page", "news.NewsPost", "blog.BlogCategory", "news.Link", (_("Media Library"), "media-library"),)),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
    ("Users", ("profile.User", "auth.Group",)),
)
# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#

# ADMIN_REMOVAL = ("mezzanine.blog.models.BlogPost",)

DASHBOARD_TAGS = (
    ("mezzanine_tags.app_list",),
    ("comment_tags.recent_comments",),
    ("mezzanine_tags.recent_actions",),
)

US_TIMEZONES = (
    ('US/Alaska', 'US/Alaska'),
    ('US/Aleutian', 'US/Aleutian'),
    ('US/Arizona', 'US/Arizona'),
    ('US/Central', 'US/Central'),
    ('US/East-Indiana', 'US/East-Indiana'),
    ('US/Eastern', 'US/Eastern'),
    ('US/Hawaii', 'US/Hawaii'),
    ('US/Indiana-Starke', 'US/Indiana-Starke'),
    ('US/Michigan', 'US/Michigan'),
    ('US/Mountain', 'US/Mountain'),
    ('US/Pacific', 'US/Pacific'),
    ('US/Pacific-New', 'US/Pacific-New'),
    ('US/Samoa', 'US/Samoa'),
)

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

# PAGE_MENU_TEMPLATES = (
#     (1, _("Top navigation bar"), "pages/menus/dropdown.html"),
#     (2, _("Left-hand tree"), "pages/menus/tree.html"),
#     (3, _("Footer"), "pages/menus/footer.html"),
# )

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
# EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         (_("Image"),),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         (_("Another name"),),
#         {"blank": True, "default": 1},
#     ),
# )

f = os.path.join(PROJECT_APP_PATH, "custom_models.py")
if os.path.exists(f):
    import sys
    import imp
    module_name = "%s.settings.custom_models" % PROJECT_APP
    module = imp.new_module(module_name)
    module.__file__ = f
    sys.modules[module_name] = module
    exec(open(f, "rb").read())
# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True

# If True, the django-modeltranslation will be added to the
# INSTALLED_APPS setting.
USE_MODELTRANSLATION = False


########################
# MAIN DJANGO SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

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

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

# Supported languages
LANGUAGES = (
    ('en', _('English')),
)

# A boolean that turns on/off debug mode. When set to ``True``, stack traces
# are displayed for error pages. Should always be set to ``False`` in
# production. Best set to ``True`` in local_settings.py
DEBUG = False

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644

IS_PRODUCTION = True

GOOGLE_ANALYTICS_ID = ''
#############
# DATABASES #
#############

DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.",
        # DB name or path to database file if using sqlite3.
        "NAME": "",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}


#########
# PATHS #
#########

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = STATIC_URL + "media/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = "%s.urls" % PROJECT_APP


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            here('templates'),
            os.path.join(PROJECT_ROOT, "templates")
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
                "us_ignite.common.context_processors.settings_available",
            ],
            "builtins": [
                "mezzanine.template.loader_tags",
            ],
        },
    },
]

if DJANGO_VERSION < (1, 9):
    del TEMPLATES[0]["OPTIONS"]["builtins"]


################
# APPLICATIONS #
################

INSTALLED_APPS = (


    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",

    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.galleries",
    "mezzanine.twitter",
    # "mezzanine.accounts",
    # "mezzanine.mobile",

    # 'easy_thumbnails',
    'compressor',
    'embed_video',
    'sorl.thumbnail',

    'us_ignite.profiles',
    'us_ignite.people',
    'us_ignite.apps',
    'us_ignite.news',
    # 'us_ignite.actionclusters',
    'us_ignite.events',
    # 'us_ignite.smart_communities',
    'us_ignite.organizations',
    'us_ignite.hubs',
    'us_ignite.awards',
    'us_ignite.sections',
    'us_ignite.testbeds',
    'us_ignite.maps',
    'us_ignite.singletons',
    'us_ignite.common',
    'us_ignite.snippets',
    'us_ignite.gctc',
    'us_ignite.resources',
    'us_ignite.relay',
    'us_ignite.programs',

    'taggit',
    'geoposition',
    'watson',
    'adminsortable',
    'registration',
    'storages',
    # 's3direct',
    # 'tinymce',
    # 'filebrowser',
)

AUTH_USER_MODEL = 'profiles.User'

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment if using internationalisation or localisation
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

#todo
# put this to heroku instead!!
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyAvABAO0_NJTlC_nIhKtAU4jKpMb7tmpIk'

PAGINATOR_PAGE_SIZE = 8

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    # disable FILEBROWSER because of S3 slowness
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.

# Instead of doing "from .local_settings import *", we use exec so that
# local_settings has full access to everything defined in this module.
# Also force into sys.modules so it's visible to Django's autoreload.

f = os.path.join(PROJECT_APP_PATH, "local_settings.py")
if os.path.exists(f):
    import sys
    import imp
    module_name = "%s.settings.local_settings" % PROJECT_APP
    module = imp.new_module(module_name)
    module.__file__ = f
    sys.modules[module_name] = module
    exec(open(f, "rb").read())


####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())


CITIES_CITY_MODEL = 'hubs.CustomCitiesModel'

CITIES_POSTAL_CODES = ['US']
CITIES_LOCALES = ['US']

# CITIES_PLUGINS = [
#     'cities.plugin.postal_code_us.Plugin',  # US postal codes need region codes remapped to match geonames
# ]

CSRF_COOKIE_HTTPONLY = True


IGNITE_MANAGERS = [
    'info@us-ignite.org',
    'jennifer.mott@us-ignite.org',
]

# Account settings:
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_REDIRECT_URL_FAILURE = '/'
LOGOUT_REDIRECT_URL = '/'

# Paginator:
PAGINATOR_PAGE_SIZE = 24

# Uplaoded file restrictions:
MAX_UPLOAD_SIZE = int(1024 * 1024 * 5)   # 5MB

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

THUMBNAIL_DEBUG = True
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.dbm_kvstore.KVStore'

THUMBNAIL_PRESERVE_FORMAT=True

# from mezzanine.conf import register_setting
#
# register_setting(
#     name="AUTHORS_BOOKS_PER_PAGE",
#     label="Authors books per page",
#     description="The number of books to show per author page.",
#     editable=True,
#     default=10,
# )

# import tinymce
# RICHTEXT_WIDGET_CLASS = 'tinymce.widgets.TinyMCE'
# TINYMCE_FILEBROWSER = False

# TINYMCE_SETUP_JS = 'tiny_mce/tiny_mce.js'
# TINYMCE_SETUP_JS = 'mezzanine/js/tinymce_setup1.js'

# TINYMCE_DEFAULT_CONFIG = {
#     # 'file_browser_callback': 'mce_filebrowser',
#     'theme': "advanced",
#     # 'skin': 'default',
# }

# S3DIRECT_DESTINATIONS = {
#     'example_destination': {
#         # REQUIRED
#         'key': 'uploads/images',
#
#         # OPTIONAL
#         'auth': lambda u: u.is_staff, # Default allow anybody to upload
#         'allowed': ['image/jpeg', 'image/png', 'video/mp4'], # Default allow all mime types
#         'bucket': 'pdf-bucket', # Default is 'AWS_STORAGE_BUCKET_NAME'
#         'acl': 'private', # Defaults to 'public-read'
#         'cache_control': 'max-age=2592000', # Default no cache-control
#         'content_disposition': 'attachment', # Default no content disposition
#         'content_length_range': (5000, 20000000), # Default allow any size
#         'server_side_encryption': 'AES256', # Default no encryption
#     }
# }

