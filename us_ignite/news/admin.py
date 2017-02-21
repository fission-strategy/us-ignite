from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.admin import blogpost_fieldsets
from mezzanine.utils.static import static_lazy as static

from models import NewsPost, Link
from copy import deepcopy
from mezzanine.core.admin import (DisplayableAdmin, OwnableAdmin,
                                  BaseTranslationModelAdmin)
from mezzanine.galleries.models import Gallery
from mezzanine.galleries.admin import GalleryImageInline

# Register your models here.

newspost_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
newspost_fieldsets[0][1]["fields"].extend(["excerpt", "content"])
newspost_fieldsets[0][1]['fields'].insert(1, 'slug')
newspost_fieldsets[0][1]['fields'].insert(2, 'user')
newspost_fieldsets[0][1]['fields'].insert(3, 'program')
newspost_fieldsets[0][1]['fields'].insert(4, 'categories_new')
newspost_fieldsets[0][1]['fields'].insert(5, 'event')
newspost_fieldsets[0][1]['fields'].insert(6, 'image')
# newspost_fieldsets[1][1]['fields'].remove("keywords")
newspost_fieldsets[1][1]['classes'] = ("collapse-open",)
# newspost_fieldsets[0][1]['fields'].insert(5, 'category_tags')

# newspost_fieldsets[0][1]['fields']
# GalleryAdmin.fieldsets = page_fieldsets


class NewsAdmin(BlogPostAdmin):
    fieldsets = newspost_fieldsets

    # class Media:
    #     css = {"all": (static("mezzanine/css/admin/gallery.css"),)}

    # inlines = (GalleryImageInline,)


class LinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(NewsPost, NewsAdmin)
admin.site.register(Link, LinkAdmin)
