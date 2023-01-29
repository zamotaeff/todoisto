import pytest


@pytest.mark.django_db
def test_user_login(client, user):
    """
    Test user auth
    :param client: Django test client
    :param user: User instance
    :return: None
    """
    password = user.password
    user.set_password(password)
    user.save()

    response = client.login(
        username=user.username,
        password=password
    )

    assert response is True
