from rest_framework import permissions

from blog.models import Post, Comment
from django.contrib.auth.models import User


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True

        return obj.author == request.user