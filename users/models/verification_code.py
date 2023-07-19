# Python/Django imports
from datetime import datetime, timedelta
from django.db import models
from setup.base_model import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class VerificationCode(BaseModel):
    code = models.CharField(max_length=6, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expires = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "Verification Codes"

    def is_expired(self):
        return datetime.utcnow().hour > self.expires.hour + 2

    def get_duration(self):
        current_hour = datetime.utcnow().hour
        expired_hour = self.expires.hour
        return current_hour - 3 > expired_hour
