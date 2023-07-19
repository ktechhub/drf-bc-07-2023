from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from users.managers import CustomUserManager

AUTH_PROVIDERS = {"facebook": "facebook", "google": "google", "email": "email"}


class CustomUser(AbstractUser):
    email = models.EmailField(_("Email Address"), unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    is_admin = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    auth_provider = models.CharField(
        max_length=120, default=AUTH_PROVIDERS.get("email")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = "Users"
        ordering = ["-id"]

    def __str__(self):
        return self.get_full_name()

    def initials(self):
        if self.first_name and self.last_name:
            return f"{(self.first_name[0] + self.last_name[0]).upper()}".upper()
        return self.username[0].upper()

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),
        }
