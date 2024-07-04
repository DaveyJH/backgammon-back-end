from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """A user's profile."""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images",
        default="../default/two-dice_nv5d5h",
    )

    class Meta:
        ordering = ["owner__username"]

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """Create a profile for a user when a new user is created."""
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
