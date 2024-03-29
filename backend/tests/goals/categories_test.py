import pytest
from django.utils import timezone
from goals.serializers import GoalCategorySerializer
from tests.factories import GoalCategoryFactory
from goals.models import GoalCategory


@pytest.mark.django_db
def test_category_create(client, get_credentials, board_participant):
    """create category test"""
    data = {
        "title": "testcat",
        "board": board_participant.board.id,
    }

    response = client.post(
        path="/goals/goal_category/create",
        data=data,
        content_type="application/json",
        HTTP_AUTHORIZATION=get_credentials
    )

    category = GoalCategory.objects.last()

    assert response.status_code == 201
    assert response.data == {
        "id": category.id,
        "created": timezone.localtime(category.created).isoformat(),
        "updated": timezone.localtime(category.updated).isoformat(),
        "title": category.title,
        "is_deleted": False,
        "board": board_participant.board.id
    }


@pytest.mark.django_db
def test_category_list(client, get_credentials, board_participant):
    """category list test"""
    categories = GoalCategoryFactory.create_batch(5, user=board_participant.user, board=board_participant.board)

    response = client.get(
        path="/goals/goal_category/list",
        HTTP_AUTHORIZATION=get_credentials
    )

    assert response.status_code == 200
    assert len(response.data) == 5


@pytest.mark.django_db
def test_category_retrieve(client, get_credentials, goal_category, board_participant):
    """category detail test"""
    response = client.get(
        path=f"/goals/goal_category/{goal_category.id}",
        HTTP_AUTHORIZATION=get_credentials
    )

    assert response.status_code == 200
    assert response.data == GoalCategorySerializer(goal_category).data


@pytest.mark.django_db
def test_category_update(client, get_credentials, goal_category, board_participant):
    """category update test"""
    new_title = "updated_title"

    response = client.patch(
        path=f"/goals/goal_category/{goal_category.id}",
        HTTP_AUTHORIZATION=get_credentials,
        data={"title": new_title},
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.data.get("title") == new_title


@pytest.mark.django_db
def test_category_delete(client, get_credentials, goal_category, board_participant):
    """category delete test"""
    response = client.delete(
        path=f"/goals/goal_category/{goal_category.id}",
        HTTP_AUTHORIZATION=get_credentials,
    )

    assert response.status_code == 204
    assert response.data is None

