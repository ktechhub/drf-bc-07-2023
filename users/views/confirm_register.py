# Python/Django imports
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model

# Local app imports
from users.models.verification_code import VerificationCode
from users.serializers.user import UserDetailSerializer
from users.serializers.verification_codes import VerificationCodeSerializer

User = get_user_model()


class ConfirmRegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerificationCodeSerializer

    def post(self, request):
        try:
            serializer = VerificationCodeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.data

            email = validated_data["email"]
            code = validated_data["code"]

            user = User.objects.filter(email=email).first()
            verify_code = VerificationCode.objects.filter(user=user, code=code).first()

            if verify_code:
                if verify_code.is_expired():
                    try:
                        verify_code.delete()
                    except:
                        pass
                    return Response(
                        {
                            "status": status.HTTP_400_BAD_REQUEST,
                            "message": "The code has expired. Kindly request a new verification code",
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                if user.is_active == False or user.is_verified == False:
                    user.is_active = True
                    user.is_verified = True
                    user.save()
                    try:
                        verify_code.delete()
                    except:
                        pass
                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "message": "Email verification successful",
                        "tokens": user.tokens(),
                        "data": UserDetailSerializer(user).data,
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "Verification code doesn't exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except VerificationCode.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "Invalid code provided",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
