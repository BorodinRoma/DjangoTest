from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_selected_role = models.BooleanField("Выбранная роль", default=False)

    def __str__(self):
        return self.user.username


class RoleAdmin(Role):
    pass


class RoleUser(Role):
    pass
