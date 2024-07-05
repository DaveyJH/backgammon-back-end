from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Winner
from .serializers import WinnerSerializer
from .filters import WinnerFilter


class WinnerList(ListCreateAPIView):
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
