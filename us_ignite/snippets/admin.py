from django import forms
from django.contrib import admin

from us_ignite.snippets.models import Snippet
from mezzanine.core.admin import DisplayableAdminForm


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'url')
    list_filter = ('status', 'is_featured', 'created')
    date_hierarchy = 'created'
    # form = SnippetAdminForm
    fieldsets = (
        (None, {
            'fields': ('name', 'status', 'slug', 'body')
        }),
        ('Extras', {
            'fields': ('url', 'url_text', 'image'),
        }),
    )

admin.site.register(Snippet, SnippetAdmin)
