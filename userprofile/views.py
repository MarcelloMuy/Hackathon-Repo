"""Imported"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Resource, Progress


@login_required
def user_profile(request):
    """This view returns the user profile page."""
    myprofile = get_object_or_404(UserProfile, user=request.user)
    resources = Resource.objects.all()

    template = 'userprofile/userprofile.html'
    context = {
        'myprofile': myprofile,
        'resources': resources,
    }

    return render(request, template, context)
