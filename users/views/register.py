from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from users.helpers import generate_code
from users.models.verification_code import VerificationCode
from users.serializers.user import RegisterSerializer


User = get_user_model()


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
        print(validated_data)
        # Check for email uniqueness
        if User.objects.filter(email=validated_data["email"]).exists():
            return Response(
                {
                    "status": status.HTTP_406_NOT_ACCEPTABLE,
                    "message": "Email Already Exists!",
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )

        if validated_data["password1"] != validated_data["password2"]:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Passwords do not match",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password1"],
            username=f"{validated_data['first_name']}-{validated_data['last_name']}".lower(),
        )

        user = User.objects.filter(email=validated_data["email"]).first()

        # Send user verification code
        if VerificationCode.objects.filter(user=user).exists():
            VerificationCode.objects.get(user=user).delete()

        user_verification_code = VerificationCode.objects.create(
            user=user, code=generate_code()
        )
        # send_email_verification_code(
        #             {
        #                 "email_to": user.email,
        #                 "verify_code": str(user_verification_code.code),
        #             }
        #         )
        return Response(
            {
                "status": status.HTTP_201_CREATED,
                "message": "Account registration is successful. Check your mail for verification code.",
            },
            status=status.HTTP_201_CREATED,
        )
