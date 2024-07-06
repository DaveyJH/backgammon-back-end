from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from backgammon_drf.permissions import (
    IsOwnerOrReadOnly,
    IsPlayerOrReadOnly,
    IsMostRecentMove
)
from .models import Move
from .serializers import MoveSerializer
from .filters import MoveFilter
from games.models import Game


class MoveList(generics.ListCreateAPIView):
    serializer_class = MoveSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsPlayerOrReadOnly]
    queryset = Move.objects.all().order_by("-updated_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    filterset_class = MoveFilter
    ordering_fields = [
        "game",
        "updated_at",
    ]
    search_fields = [
        "owner__username",
    ]

    def perform_create(self, serializer):
        game_id = serializer.validated_data['game'].id
        game = Game.objects.get(id=game_id)

        if self.request.user not in [game.player1, game.player2]:
            raise PermissionDenied("You are not a player in this game.")

        serializer.save(owner=self.request.user)


class MoveDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoveSerializer
    permission_classes = [IsOwnerOrReadOnly, IsMostRecentMove]
    queryset = Move.objects.all().order_by("-updated_at")

    def perform_update(self, serializer):
        if self.get_object().game.id != int(self.request.data["game"]):
            raise PermissionDenied("You cannot change the game of a move.")
        return super().perform_update(serializer)
