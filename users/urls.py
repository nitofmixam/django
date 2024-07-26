from django.urls import path
from . import views
from .apps import UsersConfig
from django.contrib.auth.views import LogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('password-reset/', views.UserPasswordReset.as_view(), name='password_reset_form'),
    path('password-reset/done/', views.UserPasswordResetDone.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.UserPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.UserPasswordResetComplete.as_view(), name='password_reset_complete'),
]