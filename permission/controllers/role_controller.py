from django.contrib.auth.models import User

from permission.models import RoleAdmin


class RoleAdminController:
    @staticmethod
    def create_role_admin(user: User):
        role = RoleAdmin.objects.get_or_create(user=user)[0]
        role.save()
        return role