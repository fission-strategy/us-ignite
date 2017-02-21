from django.contrib import admin
from .models import FundingPartner


class FundingPartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(FundingPartner, FundingPartnerAdmin)
