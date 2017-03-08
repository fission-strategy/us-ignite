from django.contrib import admin
from us_ignite.smart_gigabit_communities.models import Pitch
from adminsortable.admin import SortableAdmin
from mezzanine.core.forms import TinyMceWidget as TinyMCE
from django import forms


class PitchAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }


class PitchAdmin(SortableAdmin):
    list_display = ('active', 'title', 'subtitle')
    form = PitchAdminForm


admin.site.register(Pitch, PitchAdmin)
