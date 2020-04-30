from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user = instance,
            first_name = instance.username
        )
        print("Profile Updated")

post_save.connect(create_profile, sender=User, dispatch_uid="create_profile")
