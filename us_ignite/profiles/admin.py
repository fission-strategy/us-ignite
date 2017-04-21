from django.contrib import admin
from models import User, ProfileLink, Interest, UserCategory
from mezzanine.accounts.admin import UserProfileAdmin
from copy import deepcopy


class ProfileLinkInline(admin.TabularInline):
    model = ProfileLink

user_fieldsets = deepcopy(UserProfileAdmin.fieldsets)
user_fields = list(user_fieldsets[1][1]['fields'])
user_fields.insert(3, 'slug')
user_fields.insert(4, 'avatar')
user_fields.insert(5, 'website')
user_fields.insert(6, 'quote')
user_fields.insert(7, 'bio')
user_fields.insert(8, 'skills')
user_fields.insert(9, 'availability')
user_fields.insert(10, 'interests')
user_fields.insert(11, 'interests_other')
user_fields.insert(12, 'category')
user_fields.insert(13, 'categories_other')
user_fields.insert(14, 'is_public')
user_fieldsets[1][1]['fields'] = tuple(user_fields)

class UserAdmin(UserProfileAdmin):
    # list_display = ('email', 'first_name', 'last_name')
    # inlines = [ProfileLinkInline,]
    fieldsets = user_fieldsets
    filter_horizontal = ("interests", "groups", "categories_other", "user_permissions")


class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)


class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(UserCategory, UserCategoryAdmin)