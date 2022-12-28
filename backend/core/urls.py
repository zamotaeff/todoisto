from django.urls import path

from core.views import UserRegistrationView


urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
]
