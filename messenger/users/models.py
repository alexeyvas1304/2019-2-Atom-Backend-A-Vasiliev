from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    name = models.CharField(verbose_name='имя', max_length=50)
    nick = models.CharField(verbose_name='ник', max_length=50)
    avatar = models.CharField(verbose_name='ссылка на аватарку', max_length=200,null=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

