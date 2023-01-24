from goals.models import BoardParticipant, Goal, GoalCategory, Board, GoalComment
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_id == request.user.id


class BoardPermissions(permissions.IsAuthenticated):
    """Permissions to access the board"""

    def has_object_permission(self, request, view, obj: Board):
        filters: dict = {'user': request.user, 'board': obj}

        if request.method not in permissions.SAFE_METHODS:
            filters['role'] = BoardParticipant.Role.owner

        return BoardParticipant.objects.filter(**filters).exists()


class GoalCategoryPermissions(permissions.IsAuthenticated):
    """Permissions to access the category"""

    def has_object_permission(self, request, view, obj: GoalCategory):
        filters: dict = {'user': request.user, 'board': obj.board}

        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]

        return BoardParticipant.objects.filter(**filters).exists()


class GoalPermissions(permissions.IsAuthenticated):
    """Permissions to access the goal"""

    def has_object_permission(self, request, view, obj: Goal):
        filters: dict = {'user': request.user, 'board': obj.category.board}

        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [BoardParticipant.Role.owner, BoardParticipant.Role.writer]

        return BoardParticipant.objects.filter(**filters).exists()


class CommentPermissions(permissions.IsAuthenticated):
    """Permissions to access the comment"""

    def has_object_permission(self, request, view, obj: GoalComment):
        return any((
            request.method in permissions.SAFE_METHODS,
            obj.user_id == request.user.id
        ))
