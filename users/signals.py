from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.profile.save()