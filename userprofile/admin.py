"""Imported"""
from django.contrib import admin
from .models import UserProfile, Role, Resource, Progress

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
        'friendly_name',
    )


class ResourceAdmin(admin.ModelAdmin):
    """Admin Resource"""
    list_display = (
        'name',
        'link',
        'level',
    )


class ProgressAdmin(admin.ModelAdmin):
    """Admin Progress"""
    list_display = (
        'userprofile',
        'resource',
        'done',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Progress, ProgressAdmin)
