from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models.verification_code import VerificationCode

User = get_user_model()


class VerificationCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    code = serializers.CharField(max_length=6, min_length=5)

    class Meta:
        model = VerificationCode
        fields = ["email", "code"]
