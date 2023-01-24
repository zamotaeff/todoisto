from bot import views
from django.urls import path

urlpatterns = [
    path('verify', views.VerificationView.as_view(), name="verify-user"),
]
