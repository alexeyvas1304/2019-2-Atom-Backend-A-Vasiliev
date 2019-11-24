from django.db import models
from chats.models import Chat
from users.models import User


class Message(models.Model):
    user = models.ForeignKey(User, verbose_name='отправитель сообщения', on_delete=models.SET_NULL, null=True,
                             related_name='messages')
    chat = models.ForeignKey(Chat, verbose_name='чат', on_delete=models.SET_NULL, null=True, related_name='messages')
    content = models.CharField(verbose_name='содержание сообщения', max_length=5000)
    added_at = models.DateTimeField(verbose_name='дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

