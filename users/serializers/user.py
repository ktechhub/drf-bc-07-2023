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
