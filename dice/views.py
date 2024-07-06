from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import DiceRoll
from .serializers import DiceRollSerializer
from .filters import DiceRollFilter


class DiceList(ListCreateAPIView):
    serializer_class = DiceRollSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = DiceRoll.objects.all()
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend
    ]
    filterset_class = DiceRollFilter
    search_fields = [
        "game__id",
    ]

    def perform_create(self, serializer):
        """Create a dice roll."""
        game_obj = serializer.validated_data['game']

        # Check if the user is a player in the game
        if self.request.user not in [game_obj.player1, game_obj.player2]:
            raise PermissionDenied("You are not a player in this game.")

        # Check if it is the user's turn
        if (
            game_obj.dice_rolls.exists()
            and game_obj.dice_rolls.latest('created_at').owner
                == self.request.user
        ):
            raise PermissionDenied("It is not your turn.")

        serializer.save(owner=self.request.user)
