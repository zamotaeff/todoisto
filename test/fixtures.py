import base64
import pytest


@pytest.fixture
@pytest.mark.django_db
def get_credentials(client, user):
    """Получение токена для аутентификации пользователя"""
    password = user.password

    user.set_password(password)
    user.save()

    token = base64.b64encode(f'{user.username}:{password}'.encode()).decode()

    return 'Basic ' + token

# import pytest
#
#
# @pytest.fixture
# @pytest.mark.django_db
# def my_token(client, django_user_model):
#     username = "test3"
#     password = "t1r2i3g4"
#
#     django_user_model.objects.create_user(
#         username=username,
#         password=password
#     )
#     response = client.post(
#         "/core/login",
#         {"username": username, "password": password},
#         format="json"
#     )
#     return response.data.cookies["csrftoken"]
