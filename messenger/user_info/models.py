from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    name = models.CharField(max_length=50)
    nick = models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


