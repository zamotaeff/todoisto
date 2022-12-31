from django.contrib.auth import get_user_model
from rest_framework import permissions, generics, status
from rest_framework.response import Response

from core import serializers


USER_MODEL = get_user_model()


class RegistrationView(generics.CreateAPIView):
    model = USER_MODEL
    serializer_class = serializers.RegistrationSerializer


class LoginView(generics.GenericAPIView):
    model = USER_MODEL
    serializer_class = serializers.LoginSerializer

    def post(self):
        pass

    def get_object(self):
        return self.request.user


class ProfileView(generics.RetrieveUpdateAPIView):
    model = USER_MODEL
    serializer_class = serializers.ProfileSerializer


class UpdatePasswordView(generics.UpdateAPIView):
    model = USER_MODEL
    serializer_class = serializers.UpdatePasswordSerializer
