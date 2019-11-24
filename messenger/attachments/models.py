from django.db import models
from chats.models import Chat
from users.models import User
from message.models import Message


class Attachment(models.Model):
    user = models.ForeignKey(User, verbose_name='отправитель вложения', on_delete=models.SET_NULL, null=True,
                             related_name='attachments')
    chat = models.ForeignKey(Chat, verbose_name='чат', on_delete=models.SET_NULL, null=True, related_name='attachments')
    message = models.ForeignKey(Message, verbose_name='сообщение, к которому прикреплено вложение',
                                on_delete=models.SET_NULL, null=True, related_name='attachments')
    type_of_attachment = models.CharField(max_length=20, verbose_name='формат вложения')
    url = models.CharField(max_length=200, verbose_name='url вложения')

    class Meta:
        verbose_name = 'вложение'
        verbose_name_plural = 'вложения'
