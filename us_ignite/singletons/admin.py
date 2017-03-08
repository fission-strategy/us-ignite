from mezzanine.utils.admin import SingletonAdmin
from .models import SiteAlert, MailChimp
from django.contrib import admin

# Subclassing allows us to customize the admin class,
# but you could also register your model directly
# against SingletonAdmin below.
class SiteAlertAdmin(SingletonAdmin):
    pass


class MailChimpAdmin(SingletonAdmin):
    pass

# admin.site.register(SiteAlert, SiteAlertAdmin)
admin.site.register(MailChimp, MailChimpAdmin)
