from permission.controllers.role_controller import RoleAdminController
from permission.controllers.user_controller import create_admin_user


class PermissionInitializer:
    @staticmethod
    def create_admin_user():
        user = create_admin_user()
        RoleAdminController.create_role_admin(user)
