"""Imported"""
from django.contrib import admin
from .models import UserProfile, Role

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

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role, RoleAdmin)
