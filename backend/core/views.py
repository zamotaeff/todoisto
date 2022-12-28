from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

from core.serializers import UserRegistrationSerializer, UserLoginSerializer

User = get_user_model()


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserLoginView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

