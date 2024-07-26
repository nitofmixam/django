import random
import secrets
import string

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()  # сохраняем пользователя
        user.is_active = False  # устанавливаем значение "не активный"
        token = secrets.token_hex(16)  # генерируем токен
        user.token = token  # сохраняем токен в поле token в модели User
        user.save()  # сохраняем изменения в базу
        host = self.request.get_host()  # получаем хост с которого пришел пользователь
        url = f'http://{host}/users/email-confirm/{token}/'  # ссылка котоая отправится пользователю
        send_mail(
            subject='Подтверждение почты',  # тема письма
            message=f'Перейди по ссылке для подтверждения почты {url}',  # сообщение
            from_email=EMAIL_HOST_USER,  # с какого имейла отправляем
            recipient_list=[user.email]  # список имейлов на которфе отправляем
        )
        return super().form_valid(
            form)  # возвращаем родительский метод, который отправляет данные в форму и сохраняет в базу


def email_verification(request, token):
    user = get_object_or_404(User, token=token)  # получаем пользователя по токену
    user.is_active = True  # меняем статус пользователя на активный
    user.save()  # сохраняем изменения в базу
    return redirect(reverse('users:login'))


def passwords():
    """
    Генерирует случайный пароль из набора символов
    """
    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    num = random.randint(8, 15)
    password = ''.join(random.sample(symbols, num))
    return password


def reset_password(request):
    """
    Страница для сброса пароля.
    При получении POST-запроса с email, генерирует новый пароль, сохраняет его в базе, и отправляет письмо с новым паролем.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)  # eсли имейл зарегистрирован
        password = passwords()
        user.set_password(password)
        user.save()
        send_mail(
            subject='Сброс пароля',  # тема письма
            message=f' Ваш новый пароль {password}',  # сообщение
            from_email=EMAIL_HOST_USER,  # с какого имейла отправляем
            recipient_list=[user.email]  # список имейлов на которых отправляем
        )
        return redirect(reverse('users:login'))
    return render(request, 'users/reset_password.html')