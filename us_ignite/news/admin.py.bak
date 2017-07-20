from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.core.admin import DisplayableAdminForm
# from mezzanine.blog.admin import blogpost_fieldsets
# from mezzanine.utils.static import static_lazy as static

from mezzanine.blog.models import BlogPost
from models import NewsPost, Link
from copy import deepcopy
from django import forms
from mezzanine.core.models import CONTENT_STATUS_DRAFT

# from mezzanine.core.admin import (DisplayableAdmin, OwnableAdmin,
#                                   BaseTranslationModelAdmin)
# from mezzanine.galleries.models import Gallery
# from mezzanine.galleries.admin import GalleryImageInline
# from django.utils.translation import ugettext_lazy as _


# Register your models here.

newspost_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
newspost_fieldsets[0][1]['fields'].insert(1, 'slug')
newspost_fieldsets[0][1]["fields"].insert(5, 'excerpt')
newspost_fieldsets[0][1]['fields'].insert(2, 'user')
newspost_fieldsets[0][1]['fields'].insert(3, 'program')
newspost_fieldsets[0][1]['fields'].insert(5, 'event')
newspost_fieldsets[0][1]['fields'].insert(6, 'event_date')
newspost_fieldsets[0][1]['fields'].insert(7, 'image')
newspost_fieldsets[0][1]['fields'].insert(8, 'is_featured')
# newspost_fieldsets[0][1]['fields'].insert(9, 's3')

newspost_fieldsets[0][1]['fields'].remove("allow_comments")
newspost_fieldsets[2][1]['fields'].remove("keywords")
newspost_fieldsets[2][1]['fields'].remove('slug')
newspost_fieldsets[1][1]['classes'] = ("collapse-open",)
newspost_fieldsets[2][1]['classes'] = ("collapse-open",)

hidden_field_defaults = ("status", "gen_description", "allow_comments")


class NewsAdmin(BlogPostAdmin):
    fieldsets = newspost_fieldsets


class LinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(NewsPost, NewsAdmin)
admin.site.register(Link, LinkAdmin)

