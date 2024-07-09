from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Move
from profiles.models import Profile
from games.models import Game


class MoveFilter(FilterSet):
    """Filter to allow humnan-friendly query strings for the Move model."""
    player = ChoiceFilter(
        label="Player",
        field_name="owner__profile",
        choices=[]
    )
    game = ChoiceFilter(
        label="Game",
        field_name="game",
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        """Initialize the filter with the list of profiles and games."""
        super().__init__(*args, **kwargs)
        profiles = Profile.objects.all().order_by("owner")
        games = Game.objects.all().order_by("-id")
        self.filters["player"].extra["choices"] = [
            (
                profile.owner.id,
                profile.owner.username
            ) for profile in profiles
        ]
        self.filters["game"].extra["choices"] = [
            (
                game.id,
                game
            ) for game in games
        ]

    class Meta:
        fields = [
            "player",
        ]
        model = Move
