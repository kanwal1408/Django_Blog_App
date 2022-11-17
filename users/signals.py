from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProfileModel


# used to create a profile in the admin page when someone sign up or register from front end

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)
