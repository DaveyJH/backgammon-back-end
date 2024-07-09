from rest_framework import serializers
from .models import Profile
from games.models import Game


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for the Profile model."""
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    active_games_count = serializers.SerializerMethodField()
    finished_games_count = serializers.SerializerMethodField()
    total_games_count = serializers.SerializerMethodField()
    total_wins_count = serializers.SerializerMethodField()
    total_moves_made = serializers.SerializerMethodField()

    def get_active_games_count(self, obj):
        return Game.objects.filter(
            active=True,
            player1=obj.owner,
        ).count() + Game.objects.filter(
            active=True,
            player2=obj.owner,
        ).count()

    def get_finished_games_count(self, obj):
        return Game.objects.filter(
            active=False,
            player1=obj.owner,
        ).count() + Game.objects.filter(
            active=False,
            player2=obj.owner,
        ).count()

    def get_total_games_count(self, obj):
        return Game.objects.filter(
            player1=obj.owner,
        ).count() + Game.objects.filter(
            player2=obj.owner,
        ).count()

    def get_total_wins_count(self, obj):
        return Game.objects.all().filter(
            winner__owner=obj.owner,
        ).count()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_total_moves_made(self, obj):
        return obj.owner.moves.count()

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "info",
            "image",
            "is_owner",
            "active_games_count",
            "finished_games_count",
            "total_games_count",
            "total_wins_count",
            "total_moves_made",
        ]
