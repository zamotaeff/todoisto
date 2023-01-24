from django.urls import path

from core import views


urlpatterns = [
    path("signup", views.SignupView.as_view(), name="signup"),
    path("login", views.LoginView.as_view(), name="login"),
    path("profile", views.ProfileView.as_view(), name="update-retrieve-destroy-user"),
    path("update_password", views.UpdatePasswordView.as_view(), name="update_password"),
]
