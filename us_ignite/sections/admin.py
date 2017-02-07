from django.contrib import admin
from us_ignite.sections.models import *
from adminsortable2.admin import SortableAdminMixin


# Register your models here.

class HomepageFeaturedItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title',)

class HomepageProgramAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(HomepageFeaturedItem, HomepageFeaturedItemAdmin)
admin.site.register(HomepageProgram, HomepageProgramAdmin)