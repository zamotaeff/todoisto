from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


class TgUser(models.Model):
    chat_id = models.BigIntegerField(
        verbose_name="Chat ID",
        unique=True
    )
    username = models.CharField(
        verbose_name="Username",
        max_length=255,
        null=True,
        blank=True,
        default=None
    )
    user = models.ForeignKey(
        USER,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    verification_code = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        default=None
    )
