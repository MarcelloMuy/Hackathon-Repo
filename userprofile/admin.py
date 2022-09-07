"""Imported"""
from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    """Admin profile"""
    list_display = (
        'user',
    )


admin.site.register(UserProfile, UserProfileAdmin)
