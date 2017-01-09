from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.admin import blogpost_fieldsets
from models import News
from copy import deepcopy
from mezzanine.core.admin import (DisplayableAdmin, OwnableAdmin,
                                  BaseTranslationModelAdmin)

# Register your models here.

blogpost_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
blogpost_fieldsets[0][1]["fields"].extend(["excerpt", "content", "allow_comments",])

class NewsAdmin(BlogPostAdmin):
    fieldsets = blogpost_fieldsets

admin.site.register(News, NewsAdmin)
