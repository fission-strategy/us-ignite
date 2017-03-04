from django.contrib import admin
from models import User, ProfileLink, Interest, UserCategory


class ProfileLinkInline(admin.TabularInline):
    model = ProfileLink


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    inlines = [ProfileLinkInline,]
    filter_horizontal = ("interests", "groups", "categories_other", "user_permissions")


class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)


class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(UserCategory, UserCategoryAdmin)