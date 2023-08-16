from core.models import DictRefType
from permission.controllers.init_db import PermissionInitializer


class SystemInitializer:

    def create_dict_for_type(self, model_dict):
        [model_dict.objects.get_or_create(type=TYPE[0]) for TYPE in model_dict.TYPE]

    def init(self):
        self.create_dict_for_type(DictRefType)
        PermissionInitializer.create_admin_user()
