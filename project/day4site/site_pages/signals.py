from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
import os

# Create UserProfile automatically when new User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Save profile when User is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# Delete old image when updating new one
@receiver(pre_save, sender=UserProfile)
def delete_old_image(sender, instance, **kwargs):
    if not instance.pk:
        return  
    old_image = UserProfile.objects.get(pk=instance.pk).image
    new_image = instance.image
    if old_image != new_image:
        if os.path.isfile(old_image.path) and "default.png" not in old_image.path:
            os.remove(old_image.path)

# Delete image file from system when UserProfile is deleted
@receiver(post_delete, sender=UserProfile)
def delete_profile_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path) and "default.png" not in instance.image.path:
            os.remove(instance.image.path)
