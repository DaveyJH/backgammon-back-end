from django.db import models
from django.contrib.auth.models import User
from games.models import Game


class Move(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='moves'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='moves'
    )

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.owner}'s move (ID {self.id})"
