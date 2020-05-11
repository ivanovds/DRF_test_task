from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(null=True, max_length=1, choices=GENDER_CHOICES)
    bio = models.CharField(null=True, max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(null=True, max_length=30, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Signal to automatically create profile
    when we create a standard user model.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Signal to automatically update profile
    when we update a standard user model.
    """
    instance.profile.save()
