from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView

from config.settings import EMAIL_HOST_USER
from .forms import UserLoginForm, RegistrationForm
from .apps import UsersConfig
from .models import User
from django.core.mail import send_mail


# Create your views here.


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'project_name': UsersConfig.name + '/login/',
        'title': 'Авторизация'
    }


class RegisterView(FormView):
    model = User
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.success_ulr = None

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()
        if not user:
            form.add_error(None, 'User not found')
            return self.form_invalid(form)

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()

        send_mail(subject='Сброс пароля',  # тема письма
                  message=f' Ваш новый пароль {new_password}',  # сообщение
                  from_email=EMAIL_HOST_USER,  # с какого имейла отправляем
                  recipient_list=[user.email])
        return redirect(self.success_ulr)

class UserPasswordReset(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:password_reset_done')
    email_template_name = 'users/password_reset_email.html'


class UserPasswordResetDone(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class UserPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class UserPasswordResetComplete(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
