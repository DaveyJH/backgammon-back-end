from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from backgammon_drf.permissions import IsPlayerOrReadOnly
from .models import Game
from .serializers import GameSerializer
from .filters import GameFilter


class GameList(ListCreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Game.objects.all()
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend
    ]
    filterset_class = GameFilter
    search_fields = [
        "player1__username",
        "player2__username",
    ]

    def perform_create(self, serializer):
        """Create a game that includes the currently logged in user."""
        if str(self.request.user.id) not in (
                self.request.data["player1"],
                self.request.data["player2"]
        ):
            raise PermissionDenied("You cannot create games for others.")
        if self.request.data["player1"] == self.request.data["player2"]:
            raise PermissionDenied("Players must be unique.")
        serializer.save(player1=self.request.user)


class GameDetail(RetrieveUpdateAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsPlayerOrReadOnly]
    queryset = Game.objects.all()
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend
    ]
    filterset_class = GameFilter
    search_fields = [
        "player1__username",
        "player2__username",
    ]

    def perform_update(self, serializer):
        """Update a game unless players are changed."""
        if (
            self.get_object().player1.id
                != int(self.request.data["player1"])
                or self.get_object().player2.id
                != int(self.request.data["player2"])
        ):
            raise PermissionDenied("You cannot change a game's players.")
        return super().perform_update(serializer)
