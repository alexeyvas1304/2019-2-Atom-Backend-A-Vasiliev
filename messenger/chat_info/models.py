from django.db import models
from user_info.models import User


class Chat(models.Model):
    is_group_chat = models.BooleanField('групповой или нет', default=False)
    topic = models.CharField('название', max_length=60)
    last_message = models.CharField('текст последнего сообщения',max_length=5000)

    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    content = models.CharField('текст сообщения', max_length=5000)
    added_at = models.DateTimeField('дата добавления', default='1970-01-01 12:00:00')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Member (models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    last_read_message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = 'участники'


class Attachment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    type_of_attachment = models.CharField('формат', max_length=20)
    url = models.CharField('url', max_length=100)

    class Meta:
        verbose_name = 'прикрепление'
        verbose_name_plural = 'прикрипления'
