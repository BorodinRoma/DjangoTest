from django.contrib.auth.models import User

from permission.models import RoleAdmin, RoleUser, Role


class UserRoleController:


    class KeyErrorException(Exception):
        pass

    class NotAccessException(Exception):
        pass

    def __init__(self, user: User):
        self.user = user
        self.role_info = {
            'admin': {
                'model': RoleAdmin,
                'description': 'Админ',
                'role_type': 1,
                'object': None,
            },
            'user': {
                'model': RoleUser,
                'description': 'Пользователь',
                'role_type': 2,
                'object': None,
            }

        }
        self.__set_objects()

    def __set_objects(self):
        for role_name, role_dict in self.role_info.items():
            role_model = role_dict['model']
            if role_model:
                try:
                    role_dict['object'] = role_model.objects.get(user=self.user)
                except role_model.DoesNotExist:
                    role_dict['object'] = None

    def get_current_role(self) -> Role or None:
        for role_name, role_dict in self.role_info.items():
            role = role_dict['object']
            if role and role.is_selected_role:
                return role
        return None

    def change_role(self, new_role_name: str) -> None:
        role_models = {}
        for role_name, role_dict in self.role_info.items():
            role_models.update({role_name: role_dict['model']})
        try:
            role = self.role_info[new_role_name]['object']
            if role:
                Role.objects.filter(user=self.user).update(is_selected_role=False)
                role.is_selected_role = True
                role.save()
            else:
                raise UserRoleController.KeyErrorException("Некорректный запрос")
        except KeyError:
            raise UserRoleController.KeyErrorException("Некорректный запрос")


    def set_role(self) -> None:
        role = None
        for role_name, role_dict in self.role_info.items():
            role = role_dict['object']
            if role is not None and role.is_selected_role:
                role.is_selected_role = True
                role.save()
                break
        if role is None:
            raise self.NotAccessException("Нет доступа")
        role.is_selected_role = True
        role.save()

    def current_role_admin(self) -> bool:
        role = self.role_info['admin']['object']
        if role and role.is_selected_role:
            return True
        return False

    def current_role_anonymous(self) -> bool:
        roles = Role.objects.filter(user=self.user)
        if roles.exists():
            return False
        return True

    def current_role_user(self) -> bool:
        role = self.role_info['user']['object']
        if role and role.is_selected_role:
            return True
        return False


class RoleAdminController:
    @staticmethod
    def create_role_admin(user: User):
        role = RoleAdmin.objects.get_or_create(user=user)[0]
        role.save()
        return role
