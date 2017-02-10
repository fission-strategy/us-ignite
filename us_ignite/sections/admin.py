from django.contrib import admin
from us_ignite.sections.models import *
from adminsortable.admin import SortableAdmin
# Register your models here.


class HomepageFeaturedItemAdmin(SortableAdmin):
    list_display = ('title', )


class HomepageProgramAdmin(SortableAdmin):
    list_display = ('title',)


class SponsorAdmin(SortableAdmin):
    list_display = ('name', 'link')


admin.site.register(HomepageFeaturedItem, HomepageFeaturedItemAdmin)
admin.site.register(HomepageProgram, HomepageProgramAdmin)
admin.site.register(Sponsor, SponsorAdmin)
