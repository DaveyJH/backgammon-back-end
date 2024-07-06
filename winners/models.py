from django.db import models
from django.contrib.auth.models import User
from games.models import Game


class Winner(models.Model):
    """Winner model."""
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="winners"
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='winner',
        unique=True,
    )

    class Meta:
        ordering = ["game__id"]
