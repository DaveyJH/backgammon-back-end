from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from backgammon_drf.permissions import (
    IsOwnerOrReadOnly,
    IsMostRecentMove
)
from .models import Move
from .serializers import MoveSerializer
from .filters import MoveFilter


class MoveList(ListCreateAPIView):
    """List and create moves."""
    serializer_class = MoveSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Move.objects.all().order_by("-updated_at")
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend
    ]
    filterset_class = MoveFilter
    search_fields = [
        "owner__username",
    ]

    def perform_create(self, serializer):
        game_obj = serializer.validated_data['game']
        if (
            not game_obj.active
            or self.request.user not in [game_obj.player1, game_obj.player2]
        ):
            raise PermissionDenied("You are not a player in this game.")

        serializer.save(owner=self.request.user)


class MoveDetail(RetrieveUpdateDestroyAPIView):
    """Retrieve, update, and delete a move."""
    serializer_class = MoveSerializer
    permission_classes = [IsOwnerOrReadOnly, IsMostRecentMove]
    queryset = Move.objects.all()

    def perform_update(self, serializer):
        if self.get_object().game.id != int(self.request.data["game"]):
            raise PermissionDenied("You cannot change the game of a move.")
        return super().perform_update(serializer)
