from abc import ABC, abstractmethod

from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission

from permission.controllers.role_controller import UserRoleController


class Permission(ABC):
    def __init__(self, user: User):
        self._user = user

    @abstractmethod
    def check_permit(self) -> bool:
        raise NotImplementedError


class PermissionAdmin(Permission):
    def __init__(self, user):
        super().__init__(user)

    def check_permit(self) -> bool:
        return UserRoleController(self._user).current_role_admin()


class PermissionAnonymous(Permission):
    def __init__(self, user):
        super().__init__(user)

    def check_permit(self) -> bool:
        return UserRoleController(self._user).current_role_anonymous()


class PermissionUser(Permission):
    def __init__(self, user):
        super().__init__(user)

    def check_permit(self) -> bool:
        return UserRoleController(self._user).current_role_user()


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return PermissionAdmin(request.user).check_permit()


class IsUser(BasePermission):
    """
    Allows access only to users.
    """

    def has_permission(self, request, view):
        return PermissionUser(request.user).check_permit()
