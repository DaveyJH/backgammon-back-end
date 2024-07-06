from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateAPIView
)
from backgammon_drf.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(ListAPIView):
    """Profile list view."""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(RetrieveUpdateAPIView):
    """Profile detail."""
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
