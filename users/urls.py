from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from users.views.register import RegisterView

urlpatterns = [path("register/", RegisterView.as_view(), name="register")]
