"""Imported"""
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def user_profile(request):
    """This view returns the user profile page."""
    myprofile = get_object_or_404(UserProfile, user=request.user)

    template = 'userprofile/userprofile.html'
    context = {
        'myprofile': myprofile,
    }

    return render(request, template, context)
