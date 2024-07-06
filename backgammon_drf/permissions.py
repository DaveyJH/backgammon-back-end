from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsPlayerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            obj.player1 == request.user
            or obj.player2 == request.user
        )


class IsMostRecentMove(permissions.BasePermission):
    def has_object_permission(self, _, __, obj):
        if obj != obj.game.moves.latest('updated_at'):
            raise PermissionDenied("This is not the most recent move.")
        return True
