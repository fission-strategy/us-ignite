from copy import deepcopy

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin, PageAdminForm, LinkAdmin
from mezzanine.pages.models import RichTextPage, Link
from mezzanine.blog.models import BlogPost
from mezzanine.generic.models import ThreadedComment
from mezzanine.core.forms import TinyMceWidget

from us_ignite.common.models import LinkResource

from taggit.models import Tag


class LinkInline(admin.StackedInline):
    model = LinkResource


class RichTextPageForm(PageAdminForm):
    class Meta:
        model = RichTextPage
        widgets = {
            'description': TinyMceWidget(),
        }
        fields = '__all__'


form_fieldsets = deepcopy(PageAdmin.fieldsets)
form_fieldsets[0][1]['fields'].insert(1, 'slug')
form_fieldsets[0][1]['fields'].insert(2, 'description')
form_fieldsets[1][1]['fields'].remove('slug')
form_fieldsets[1][1]['fields'].remove('keywords')
#remove description from metadata box
form_fieldsets[1][1]['fields'].pop(1)

PageAdmin.inlines = [LinkInline, ]
PageAdmin.form = RichTextPageForm
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
