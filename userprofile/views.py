from django.shortcuts import render

# Create your views here.


def user_profile(request):
    """This view returns the user profile page."""
    return render(request, 'userprofile/userprofile.html')
