"""Imported"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class Role(models.Model):
    """A model for user role options"""
    name = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """A user profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    level = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )

    def __str__(self):
        return self.user.username


class Resource(models.Model):
    """A model for user role options"""
    name = models.CharField(max_length=250)
    link = models.URLField()
    roles = models.ManyToManyField(Role)
    level = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    print('receiver called')
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
