from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Winner
from profiles.models import Profile


class WinnerFilter(FilterSet):
    winner = ChoiceFilter(
        label="Winner",
        field_name="owner__profile",
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        profiles = Profile.objects.all().order_by("owner")
        # Create choices dynamically
        self.filters["winner"].extra['choices'] = [
            (
                profile.owner.id,
                profile.owner.username
            ) for profile in profiles
        ]

    class Meta:
        fields = [
            "winner",
        ]
        model = Winner
