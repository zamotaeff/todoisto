from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=150,
                                  verbose_name='Имя',
                                  null=True,
                                  blank=True)
    last_name = models.CharField(max_length=150,
                                 verbose_name='Фамилия',
                                 null=True,
                                 blank=True)
    username = models.CharField(max_length=150,
                                verbose_name='Никнейм',
                                unique=True)
    password = models.CharField(max_length=250,
                                verbose_name='Пароль')
    email = models.EmailField(verbose_name='email address',
                              max_length=250,
                              blank=True,
                              null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username}'

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
