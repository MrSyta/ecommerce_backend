from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group_name):
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])


class IsAdminOrReadOnly(permissions.BasePermission):
    message = "Only admin can CREATE, UPDATE or DELETE"
    required_groups = ['admin']

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return _has_group_permission(request.user, self.required_groups)
