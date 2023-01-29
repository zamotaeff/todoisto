import factory

from core.models import User
from goals.models import Goal, GoalCategory, Board, BoardParticipant, GoalComment


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")

    class Meta:
        model = User


class BoardFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence", nb_words=2)
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
    title = factory.Faker("sentence", nb_words=2)
    is_deleted = False
    user = factory.SubFactory(UserFactory)
    board = factory.SubFactory(BoardFactory)

    class Meta:
        model = GoalCategory


class GoalFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence", nb_words=2)
    description = factory.Faker("text")
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(GoalCategoryFactory)
    status = 1
    priority = 2
    due_date = None

    class Meta:
        model = Goal


class GoalCommentFactory(factory.django.DjangoModelFactory):
    text = factory.Faker("text")
    goal = factory.SubFactory(GoalFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = GoalComment
