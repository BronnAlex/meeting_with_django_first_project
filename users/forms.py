from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    """Класс формы регистрации пользователя в представлениях создания"""

    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")
