
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth import get_user_model

from apps.users.models import Profile
User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args ,**kwargs):
    """Signal create a Profile for each new user."""
    if created:
        # Profile.objects.create(user=User)
        user_profile = Profile(user=instance)
        user_profile.save()

