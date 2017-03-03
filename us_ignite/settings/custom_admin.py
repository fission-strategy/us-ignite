from copy import deepcopy

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage
from mezzanine.blog.models import BlogPost
from mezzanine.generic.models import ThreadedComment

from taggit.models import Tag


form_fieldsets = deepcopy(PageAdmin.fieldsets)
form_fieldsets[0][1]['fields'].insert(1, 'slug')
form_fieldsets[1][1]['fields'].remove('slug')
form_fieldsets[1][1]['fields'].remove('keywords')
PageAdmin.fieldsets = form_fieldsets

# remove standard "BlogPost" since we are using the extended version called "NewsPost"
admin.site.unregister(BlogPost)
admin.site.unregister(ThreadedComment)

admin.site.unregister(RichTextPage)
admin.site.unregister(Tag)
admin.site.register(RichTextPage, PageAdmin)
