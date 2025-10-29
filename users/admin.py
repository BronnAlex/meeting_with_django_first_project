from django.contrib import admin

from users.models import CustomUser


# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Класс регистрации кастомного пользователя в админке"""

    list_display = (
        "id",
        "email",
    )
