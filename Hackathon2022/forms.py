from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    ROLES = [
        ('young_coder', 'Young Coder'),
        ('college_student', 'College Student'),
        ('career_change', 'Career Change'),
    ]
    role = forms.ChoiceField(label='Who are You?', choices=ROLES)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.role = self.cleaned_data['role']
        user.save()
        return user
