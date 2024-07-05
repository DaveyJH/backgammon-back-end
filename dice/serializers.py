from rest_framework import serializers
from .models import DiceRoll


class DiceRollSerializer(serializers.ModelSerializer):
    value1 = serializers.IntegerField(read_only=True)
    value2 = serializers.IntegerField(read_only=True)

    class Meta:
        model = DiceRoll
        fields = [
            "id",
            "game",
            "value1",
            "value2",
        ]
