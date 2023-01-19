from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from goals import models
from goals import serializers
from goals.filters import GoalDateFilter


class GoalCategoryCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
    queryset = models.GoalCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
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
        instance.is_delete = True
        instance.save(update_fields=("is_deleted",))
        models.Goal.objects.filter(category=instance).update(status=models.Status.archived)
        return instance


class GoalCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCreateSerializer


class GoalListView(ListAPIView):
    queryset = models.Goal.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]
    filterset_class = GoalDateFilter
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]

    def get_queryset(self):
        return models.Goal.objects.filter(
            user=self.request.user
        ).exclude(status=models.Status.archived)


class GoalView(RetrieveUpdateDestroyAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Goal.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        instance.status = models.Status.archived
        instance.save(update_fields=("status",))

        return instance


class GoalCommentCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCommentCreateSerializer


class GoalCommentListView(ListAPIView):
    queryset = models.GoalComment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCommentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        OrderingFilter,
        SearchFilter,
    ]
    filterset_fields = ["goal"]
    ordering = ["-created"]

    def get_queryset(self):
        return models.GoalComment.objects.filter(user=self.request.user)


class GoalCommentView(RetrieveUpdateDestroyAPIView):
    queryset = models.GoalComment.objects.all()
    serializer_class = serializers.GoalCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.GoalComment.objects.filter(user=self.request.user)