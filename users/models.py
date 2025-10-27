from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите ваш email"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        help_text="Загрузите ваш автар",
        blank=True,
        null=True,
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        help_text="Укажите Вашу страну",
        blank=True,
        null=True,
    )

    token = models.CharField(
        max_length=100, verbose_name="Токен", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользовател"

    def __str__(self):
        return self.email
