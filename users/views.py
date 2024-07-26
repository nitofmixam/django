from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
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


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            field = form.cleaned_data
            send_mail(
                "Congratulations! You have registered in Sky.pro sales of optical goods",
                f"""Hi, {field.get('username')}. This is a test e-mail from Sky.pro optic to Sky.
                Your email: {field.get('email')}.
                Your password: {field.get('password1')}."
                'Remember to change it after login.""",
                '21cfk8lf6gbp@mail.ru',
                [field.get('email'), 'ice_eyes@mail.ru'],
                fail_silently=False,
            )
        return super().form_valid(form)


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


