from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """Game model with two players."""
    player1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='player1'
    )
    player2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='player2'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default/backgammon-starting-board-with-direction_jqwtuy',
        blank=True,
    )
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'Game #{self.id} : {self.player1} vs. {self.player2}'
