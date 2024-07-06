from random import randint
from django.db import models
from django.contrib.auth.models import User
from games.models import Game


class DiceRoll(models.Model):
    """Double dice random roll model."""
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='dice_rolls'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dice_rolls'
    )
    value1 = models.IntegerField()
    value2 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.value1 = randint(1, 6)
            self.value2 = randint(1, 6)
            super().save(*args, **kwargs)

    def __str__(self):
        return f'Die 1: {self.value1}\nDie 2: {self.value2}'

    class Meta:
        ordering = ['-created_at']
