from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User (AbstractBaseUser):
    name = models.CharField(max_length=50)
    nick = models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)


