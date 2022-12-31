from django.contrib.auth import get_user_model, login
from rest_framework import permissions, generics, status
from rest_framework.response import Response

from core import serializers


USER_MODEL = get_user_model()


class RegistrationView(generics.CreateAPIView):
    model = USER_MODEL
    serializer_class = serializers.RegistrationSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)

        return Response(serializer.data)


class ProfileView(generics.RetrieveUpdateAPIView):
    model = USER_MODEL
    serializer_class = serializers.ProfileSerializer


class UpdatePasswordView(generics.UpdateAPIView):
    model = USER_MODEL
    serializer_class = serializers.UpdatePasswordSerializer
