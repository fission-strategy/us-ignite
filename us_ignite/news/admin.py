from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.admin import blogpost_fieldsets
from models import NewsPost
from copy import deepcopy
from mezzanine.core.admin import (DisplayableAdmin, OwnableAdmin,
                                  BaseTranslationModelAdmin)

# Register your models here.

newspost_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
newspost_fieldsets[0][1]["fields"].extend(["excerpt", "content",])
newspost_fieldsets[0][1]['fields'].insert(1, 'slug')
newspost_fieldsets[0][1]['fields'].insert(2, 'user')
newspost_fieldsets[0][1]['fields'].insert(4, 'image')


class NewsAdmin(BlogPostAdmin):
    fieldsets = newspost_fieldsets

admin.site.register(NewsPost, NewsAdmin)
