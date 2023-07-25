from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from users.views.register import RegisterView
from users.views.confirm_register import ConfirmRegisterView
from users.views.login import LoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("confirm-register/", ConfirmRegisterView.as_view(), name="confirm-register"),
    path("login/", LoginView.as_view(), name="login"),
]
