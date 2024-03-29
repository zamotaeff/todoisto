import pytest
from core.serializers import ProfileSerializer


@pytest.mark.django_db
def test_user_profile(client, get_credentials, user):
    """
    Test user profile
    :param client: Django test client
    :param get_credentials: Function to get user token for auth
    :param user: User instance
    :return: None
    """
    response = client.get(
        path="/core/profile",
        HTTP_AUTHORIZATION=get_credentials
    )

    assert response.status_code == 200
    assert response.data == ProfileSerializer(user).data
