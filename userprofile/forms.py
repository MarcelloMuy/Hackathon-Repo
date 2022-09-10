from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    '''Create a Django form'''
    class Meta:
        '''Use userprofile module and specific fields to create form'''
        model = UserProfile
        fields = [
            'role',
            ]
        labels = {
            'role': ('Who are You?')
        }
