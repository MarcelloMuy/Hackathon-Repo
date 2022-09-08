"""Imported"""
from django.contrib import admin
from .models import UserProfile, Role, Resource

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    """Admin profile"""
    list_display = (
        'user',
    )


class RoleAdmin(admin.ModelAdmin):
    """Admin Role"""
    list_display = (
        'name',
        'desc',
    )


class ResourceAdmin(admin.ModelAdmin):
    """Admin Resource"""
    list_display = (
        'name',
        'link',
        'level',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Resource, ResourceAdmin)
