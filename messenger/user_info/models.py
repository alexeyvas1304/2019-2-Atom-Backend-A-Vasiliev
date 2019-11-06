from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    name = models.CharField('имя', max_length=50)
    nick = models.CharField('ник', max_length=50)
    avatar = models.CharField('ссылка на аватарку', max_length=100)
    reg_date = models.DateTimeField('дата регистрации', default='1970-01-01 12:00:00')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


