from rest_framework import serializers
from .models import Move


class MoveSerializer(serializers.ModelSerializer):
    """Serializer for the Move model."""
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Move
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "content",
            "is_owner",
            "profile_id",
            "profile_image",
            "game",
        ]
