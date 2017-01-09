from copy import deepcopy

from django.contrib import admin

from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost

form_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
form_fieldsets[0][1]['fields'].insert(1, 'slug')
form_fieldsets[0][1]['fields'].insert(2, 'user')
form_fieldsets[0][1]['fields'].insert(4, 'image')
form_fieldsets[0][1]['fields'].insert(4, 'excerpt')
form_fieldsets[2][1]['fields'].remove('slug')
BlogPostAdmin.fieldsets = form_fieldsets

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, BlogPostAdmin)
