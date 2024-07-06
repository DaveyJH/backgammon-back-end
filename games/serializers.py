from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Game
from moves.models import Move


class GameSerializer(serializers.ModelSerializer):
    all_moves = serializers.SerializerMethodField()
    latest_move_id = serializers.SerializerMethodField()
    time_since_last_move = serializers.SerializerMethodField()

    def get_all_moves(self, obj):
        return obj.moves.all().values()

    def get_latest_move_id(self, obj):
        try:
            return obj.moves.latest("updated_at").id
        except Move.DoesNotExist:
            return None

    def get_time_since_last_move(self, obj):
        try:
            return naturaltime(obj.moves.latest("updated_at").updated_at)
        except Move.DoesNotExist:
            return None

    class Meta:
        model = Game
        fields = [
            "id",
            "player1",
            "player2",
            "created_at",
            "updated_at",
            "image",
            "winner",
            "active",
            "all_moves",
            "latest_move_id",
            "time_since_last_move",
            "dice_rolls",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "active",
            "all_moves",
            "latest_move_id",
            "time_since_last_move",
            "dice_rolls",
        ]
