"""WSGI config for us_ignite project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework."""

import os
import sys
from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
from django.core.management import execute_from_command_line

if __name__ == "__main__":

    from mezzanine.utils.conf import real_project_name

    settings_module = "%s.production" % real_project_name("us_ignite.settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "us_ignite.settings")

    execute_from_command_line(sys.argv)
# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
