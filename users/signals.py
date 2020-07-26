from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# we need a profile to be created for each new user
@receiver(post_save, sender=User)   #(signal, sender)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)   #(signal, sender)
def save_profile(sender, instance,  **kwargs):
	instance.profile.save()