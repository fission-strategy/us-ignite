from mezzanine.utils.admin import SingletonAdmin
from .models import SiteAlert
from django.contrib import admin

# Subclassing allows us to customize the admin class,
# but you could also register your model directly
# against SingletonAdmin below.
class SiteAlertAdmin(SingletonAdmin):
    pass

admin.site.register(SiteAlert, SiteAlertAdmin)