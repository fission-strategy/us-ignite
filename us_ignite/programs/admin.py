from django.contrib import admin
from .models import Program, FundingPartner, Link


class LinkInline(admin.StackedInline):
    model = Link


class FundingPartnerInline(admin.StackedInline):
    model = FundingPartner


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'default')
    inlines = [LinkInline, FundingPartnerInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Program, ProgramAdmin)
