from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Доступ на чтение для всех, изменения только для автора."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
