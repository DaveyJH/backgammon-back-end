from django.db.models import Q
from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Game
from profiles.models import Profile


class GameFilter(FilterSet):
    player1 = ChoiceFilter(
        label="Player 1",
        field_name="player1__profile",
        choices=[]
    )
    player2 = ChoiceFilter(
        label="Player 2",
        field_name="player2__profile",
        choices=[]
    )
    either_player = ChoiceFilter(
        label="Either player",
        method="filter_either_player",
        choices=[]
    )
    winner = ChoiceFilter(
        label="Winner",
        field_name="winner__owner__profile",
        choices=[]
    )
    is_active = ChoiceFilter(
        label="Active game?",
        field_name="active",
        choices=(
            (True, "yes"),
            (False, "no"),
        )
    )

    def __init__(self, *args, **kwargs):
        """Initialize the filter with the list of profiles."""
        super().__init__(*args, **kwargs)
        profiles = Profile.objects.all().order_by("owner")
        filters = [
            "player1",
            "player2",
            "winner",
            "either_player"
        ]
        for filter in filters:
            self.filters[filter].extra['choices'] = [
                (
                    profile.owner.id,
                    profile.owner.username
                ) for profile in profiles
            ]

    def filter_either_player(self, queryset, name, value):
        """Filter games where the player is either player1 or player2."""
        return queryset.filter(
            Q(player1_id=value) |
            Q(player2_id=value)
        )

    class Meta:
        fields = [
            "either_player",
            "player1",
            "player2",
            "winner",
            "is_active",
        ]
        model = Game
