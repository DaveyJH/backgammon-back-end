from django.db import models
from django.contrib.auth.models import User


class Winner(models.Model):
    """Winner model."""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
