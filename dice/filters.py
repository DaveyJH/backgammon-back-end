from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import DiceRoll
from games.models import Game


class DiceRollFilter(FilterSet):
    game = ChoiceFilter(
        label="Game",
        field_name="game__id",
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        games = Game.objects.all().order_by("id")
        # Create choices dynamically
        self.filters["game"].extra['choices'] = [
            (
                game.id,
                game
            ) for game in games
        ]

    class Meta:
        fields = [
            "game",
        ]
        model = DiceRoll
