import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import CustomUser


class UserCreateView(CreateView):
    """Регистрация пользователя"""

    model = CustomUser
    form_class = UserRegisterForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:login")

    # переопределяем метод валидации
    def form_valid(self, form):

        # user = form.save(form)  # сохраняем пользователя, грубый метод, т.к не дает возможность нормально обрабатывать экземпляр
        user = form.save(commit=False) # измененный вариант выше, не сразу сохраняет данные, которые в последствии можно изменять
        user.is_active = False  # doing user not active
        user.token = secrets.token_hex(16)  # generate token
        user.save()
        host = self.request.get_host()  # получение хоста, откуда пришел пользователь
        # Реализуем ссылку для перехода с токеном, для того, чтобы сделать пользователя активным
        url = f"http://{host}/users/email-confirm/{user.token}/"  # Эты ссылка отправится пользователю, для верификации
        # Импортированная функция для отправки сообщения
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейдите по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[
                user.email,
            ],  # список email(ов) пользователей
        )

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
