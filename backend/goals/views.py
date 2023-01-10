from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from goals import models
from goals import serializers


class GoalCategoryCreateView(CreateAPIView):
    model = models.GoalCategory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCreateSerializer

