from rest_framework import serializers
from .models import DiceRoll


class DiceRollSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiceRoll
        fields = [
            "id",
            "game",
            "value1",
            "value2",
            "owner",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "value1",
            "value2",
            "created_at",
            "owner",
        ]
