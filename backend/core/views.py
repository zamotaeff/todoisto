from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from core.serializers import UserRegistrationSerializer

User = get_user_model()


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
