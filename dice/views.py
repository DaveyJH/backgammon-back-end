from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import DiceRoll
from .serializers import DiceRollSerializer
from .filters import DiceRollFilter


class DiceList(ListCreateAPIView):
    serializer_class = DiceRollSerializer
    queryset = DiceRoll.objects.all()
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend
    ]
    filterset_class = DiceRollFilter
    search_fields = [
        "game__id",
    ]
