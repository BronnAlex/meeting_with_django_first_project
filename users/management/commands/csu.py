from django.core.management import BaseCommand

from users.models import CustomUser


# python manage.py csu - в командной строке для регистрации суперпользователя(админа)
# Регистрацию простого пользователя делаем через контроллер
class Command(BaseCommand):
    """Создание суперпользователя"""

    def handle(self, *args, **options):
        user = CustomUser.objects.create(email="admin@example.com")
        user.set_password("123qwerty")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
