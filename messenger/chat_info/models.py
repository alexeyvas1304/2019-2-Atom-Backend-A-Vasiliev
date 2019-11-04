from django.db import models
from user_info.models import User


class Chat(models.Model):
    is_group_chat = models.BooleanField(default=False)
    topic = models.CharField(max_length=60)
    last_message = models.CharField(max_length=5000)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=5000)
    added_at = models.DateTimeField(default='1970-01-01 12:00:00')


class Member (models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    last_read_message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)


class Attachment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    type_of_attachment= models.CharField(max_length=20)
    url = models.CharField(max_length=100)
