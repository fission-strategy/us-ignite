from django.contrib import admin
from us_ignite.sections.models import *


# Register your models here.

class HomepageFeaturedItemAdmin(admin.ModelAdmin):
    list_display = ('title',)


class HomepageProgramAdmin(admin.ModelAdmin):
    list_display = ('title',)


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'link')


admin.site.register(HomepageFeaturedItem, HomepageFeaturedItemAdmin)
admin.site.register(HomepageProgram, HomepageProgramAdmin)
admin.site.register(Sponsor, SponsorAdmin)
