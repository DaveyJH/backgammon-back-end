from rest_framework import permissions


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
            obj.game.player1 == request.user
            or obj.game.player2 == request.user
        )


class IsMostRecentMove(permissions.BasePermission):
    def has_object_permission(self, _, __, obj):
        return obj == obj.game.moves.latest('updated_at')
