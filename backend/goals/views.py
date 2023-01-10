from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from goals import models
from goals import serializers


class GoalCategoryCreateView(CreateAPIView):
    queryset = models.GoalCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCreateSerializer


class GoalCategoryListView(ListAPIView):
    queryset = models.GoalCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]

    def get_queryset(self):
        return models.GoalCategory.objects.filter(
            user=self.request.user, is_deleted=False
        )


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    queryset = models.GoalCategory.objects.all()
    serializer_class = serializers.GoalCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.GoalCategory.objects.filter(user=self.request.user,
                                                  is_deleted=False)

    def perform_destroy(self, instance):
        # Not remove category
        instance.is_deleted = True
        instance.save()
        return instance
