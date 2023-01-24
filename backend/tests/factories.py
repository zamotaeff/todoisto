import factory

from core.models import User
from goals.models import Goal, GoalCategory, Board, BoardParticipant, GoalComment


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("name")
    first_name = "first name"
    last_name = "last name"
    email = "mail@mail.ru"
    password = "AnyPass2022"

    class Meta:
        model = User


class BoardFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("name")
    is_deleted = False

    class Meta:
        model = Board


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    board = factory.SubFactory(BoardFactory)
    user = factory.SubFactory(UserFactory)
    role = 1

    class Meta:
        model = BoardParticipant


class GoalCategoryFactory(factory.django.DjangoModelFactory):
    title = "test category"
    is_deleted = False
    user = factory.SubFactory(UserFactory)
    board = factory.SubFactory(BoardFactory)

    class Meta:
        model = GoalCategory


class GoalFactory(factory.django.DjangoModelFactory):
    title = "goal"
    description = "description"
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(GoalCategoryFactory)
    status = 1
    priority = 2
    due_date = None

    class Meta:
        model = Goal


class GoalCommentFactory(factory.django.DjangoModelFactory):
    text = "test comment"
    goal = factory.SubFactory(GoalFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = GoalComment
