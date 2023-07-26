from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100, min_length=4)
    first_name = serializers.CharField(max_length=170, min_length=3)
    last_name = serializers.CharField(max_length=170, min_length=3)
    password1 = serializers.CharField(
        min_length=6, required=True, style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        min_length=6, required=True, style={"input_type": "password"}
    )


class UserDetailSerializer(serializers.ModelSerializer):
    """User Details Serializer"""

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "auth_provider",
            "is_admin",
            "is_verified",
            "is_active",
            "last_login",
            "date_joined",
        ]
        read_only_fields = (
            "email",
            "is_admin",
            "last_login",
            "date_joined",
            "is_active",
            "is_verified",
        )


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=6, required=True, style={"input_type": "password"}
    )
    email = serializers.EmailField(max_length=120, min_length=4)

    class Meta:
        model = User
        fields = ["email", "password"]
