from django.contrib.auth import login, logout, authenticate
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from core.models import User
from core import serializers


class SignupView(generics.CreateAPIView):
    serializer_class = serializers.CreateUserSerializer


class LoginView(generics.CreateAPIView):
    """Login user"""
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        # validate request data
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # authenticate
        username = request.data.get('username')
        password = request.data.get('password')

        # auth
        user = authenticate(request, username=username, password=password)

        # login
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(data={'password': ['Invalid password']}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> User:
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UpdatePasswordSerializer

    def get_object(self):
        return self.request.user
