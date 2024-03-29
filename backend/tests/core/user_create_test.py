import pytest
from tests.factories import UserFactory


@pytest.mark.django_db
def test_user_create(client, django_user_model):
    """
    Test user create
    :param client: Django test client
    :param django_user_model: Django user model
    :return: None
    """
    data = {
        "username": "test_user",
        "password": "p1o2i3u4",
        "password_repeat": "p1o2i3u4",
    }

    response = client.post(
        path="/core/signup",
        data=data,
        content_type="application/json"
    )

    user = django_user_model.objects.last()

    assert response.status_code == 201
    assert response.data == {
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }
