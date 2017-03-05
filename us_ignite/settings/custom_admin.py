from copy import deepcopy

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin, PageAdminForm, LinkAdmin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.pages.models import RichTextPage, Link
from mezzanine.blog.models import BlogPost
from us_ignite.news.admin import NewsAdmin
from us_ignite.news.models import NewsPost
from mezzanine.generic.models import ThreadedComment
from mezzanine.core.forms import TinyMceWidget
# from tinymce.widgets import TinyMCE as TinyMceWidget
# from s3direct.widgets import S3DirectWidget

from us_ignite.common.models import LinkResource

from taggit.models import Tag


class LinkInline(admin.StackedInline):
    model = LinkResource


form_fieldsets = deepcopy(PageAdmin.fieldsets)
form_fieldsets[0][1]['fields'].insert(1, 'slug')
form_fieldsets[1][1]['fields'].remove('slug')
form_fieldsets[1][1]['fields'].remove('keywords')
#remove description from metadata box
form_fieldsets[1][1]['fields'].pop(1)

PageAdmin.inlines = [LinkInline, ]
PageAdmin.fieldsets = form_fieldsets
LinkAdmin.inlines = []


# remove standard "BlogPost" since we are using the extended version called "NewsPost"
admin.site.unregister(BlogPost)
admin.site.unregister(ThreadedComment)

admin.site.unregister(RichTextPage)
admin.site.unregister(Tag)
admin.site.register(RichTextPage, PageAdmin)
admin.site.unregister(Link)
admin.site.register(Link, LinkAdmin)
