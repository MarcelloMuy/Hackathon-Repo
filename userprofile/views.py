"""Imported"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Resource, Role
from .forms import UserProfileForm


@login_required
def user_profile(request):
    """This view returns the user profile page."""
    myprofile = get_object_or_404(UserProfile, user=request.user)
    resources = Resource.objects.all()
    roles = Role.objects.all()

    form = UserProfileForm(request.POST or None, instance=myprofile)
    if request.method == 'POST':
        if form.is_valid():
            # form.instance.user = request.user
            form.role = request.POST.get('role')
            form.save()

    template = 'userprofile/userprofile.html'
    context = {
        'myprofile': myprofile,
        'resources': resources,
        'roles': roles,
        'form': form,
    }

    return render(request, template, context)
