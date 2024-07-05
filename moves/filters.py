from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Move
from profiles.models import Profile


class MoveFilter(FilterSet):
    player = ChoiceFilter(
        label="Player",
        field_name="owner__profile",
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        profiles = Profile.objects.all().order_by("owner")
        # Create choices dynamically
        self.filters["player"].extra["choices"] = [
            (
                profile.owner.id,
                profile.owner.username
            ) for profile in profiles
        ]

    class Meta:
        fields = [
            "player",
        ]
        model = Move
