# Python/Django imports
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model

# Local app imports
from users.models.verification_code import VerificationCode
from users.serializers.user import LoginSerializer, UserDetailSerializer
from users.helpers import (
    generate_code,
    send_email_verification_code,
)

User = get_user_model()


class LoginView(generics.GenericAPIView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework

    Accept the following POST parameters: email, password
    Return the REST Framework Token Object's key.
    """

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data

        user = User.objects.filter(email=validated_data["email"]).first()
        if user and not user.check_password(validated_data["password"]):
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Please enter the correct email and password. Note that both fields may be case-sensitive.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user:
            if not user.is_active:
                # Check if user already have a code
                if VerificationCode.objects.filter(user=user).exists():
                    VerificationCode.objects.get(user=user).delete()

                user_verification_code = VerificationCode.objects.create(
                    user=user, code=generate_code()
                )
                send_email_verification_code(
                    {
                        "name": user.get_full_name(),
                        "email": user.email,
                        "verify_code": str(user_verification_code.code),
                    }
                )
                return Response(
                    {
                        "status": status.HTTP_401_UNAUTHORIZED,
                        "message": "Email is not verified or account is in active. Kindly verify first.",
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            # Restricting login for email AUTH_PROVIDERS only
            if user.auth_provider != "email":
                return Response(
                    {
                        "status": status.HTTP_403_FORBIDDEN,
                        "message": "This account doesn't allow password authentication. Kindly login with your provider",
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )

            tokens = user.tokens()
            data = {
                "status": status.HTTP_200_OK,
                "message": "Login successful",
                "access_token": tokens["access_token"],
                "refresh_token": tokens["refresh_token"],
                "data": UserDetailSerializer(user).data,
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Please enter the correct email and password. Note that both fields may be case-sensitive",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
