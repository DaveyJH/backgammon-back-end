from rest_framework import serializers
from .models import Winner


class WinnerSerializer(serializers.ModelSerializer):
    """Serializer for the Winner model."""
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Winner
        fields = [
            "id",
            "owner",
            "is_owner",
            "game",
        ]
