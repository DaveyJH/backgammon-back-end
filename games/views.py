from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from backgammon_drf.permissions import IsPlayerOrReadOnly
from .models import Game
from .serializers import GameSerializer
from .filters import GameFilter


class GameList(ListCreateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend
        # todo - add ordering with number of moves (multiple files)
    ]
    filterset_class = GameFilter
    search_fields = [
        "player1__username",
        "player2__username",
    ]


class GameDetail(RetrieveUpdateAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsPlayerOrReadOnly]
    queryset = Game.objects.all()
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend
        # todo - add ordering with number of moves (multiple files)
    ]
    filterset_class = GameFilter
    search_fields = [
        "player1__username",
        "player2__username",
    ]
