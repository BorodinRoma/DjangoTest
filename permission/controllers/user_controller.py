import random
import string

from django.contrib.auth.models import User


def create_admin_user() -> User:
    try:
        user = User.objects.get(username="admin")
    except User.DoesNotExist:
        user = User.objects.create_superuser('admin', 'admin@mail.ru', 'qwer1234')
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
    return user


def create_password() -> str:
    sizes = range(12, 20)
    size = random.choice(sizes)
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(size))