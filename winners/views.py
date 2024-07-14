from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import Winner
from .serializers import WinnerSerializer
from .filters import WinnerFilter


class WinnerList(ListCreateAPIView):
    """List and create winners."""
    serializer_class = WinnerSerializer
    queryset = Winner.objects.all()
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend
    ]
    filterset_class = WinnerFilter
    search_fields = [
        "owner__username",
    ]

    def perform_create(self, serializer):
        """Create a winner unless user is not a player in the game."""
        game_obj = serializer.validated_data['game']

        if self.request.user not in [game_obj.player1, game_obj.player2]:
            raise PermissionDenied("You are not a player in this game.")

        serializer.save()
