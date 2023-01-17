from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from goals import models
from goals import serializers
from goals import filters


class GoalCategoryCreateView(CreateAPIView):
    queryset = models.GoalCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
    queryset = models.GoalCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
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

        # Change status for all goals of category
        goals = models.Goal.objects.filter(category=instance)
        for goal in goals:
            goal.status = models.Status.archived
        models.Goal.objects.bulk_update(goals, ['status'])

        # Not remove category
        instance.is_deleted = True
        instance.save()

        return instance


class GoalCreateView(CreateAPIView):
    queryset = models.Goal.objects.all()
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
    filterset_class = filters.GoalDateFilter
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]

    def get_queryset(self):
        return models.Goal.objects.filter(
            user=self.request.user
        ).exclude(status=models.Goal.Status.archived)


class GoalView(RetrieveUpdateDestroyAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Goal.objects.filter(user=self.request.user)


class GoalCommentCreateView(CreateAPIView):
    queryset = models.GoalComment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCommentCreateSerializer


class GoalCommentListView(ListAPIView):
    queryset = models.GoalComment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GoalCommentSerializer
    pagination_class = LimitOffsetPagination


class GoalCommentView(RetrieveUpdateDestroyAPIView):
    queryset = models.GoalComment.objects.all()
    serializer_class = serializers.GoalCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
