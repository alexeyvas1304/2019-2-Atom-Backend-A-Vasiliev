from django.db import models
from users.models import User


class Chat(models.Model):
    is_group_chat = models.BooleanField(verbose_name='групповой или нет', default=False)
    topic = models.CharField(verbose_name='название', max_length=60)
    last_message = models.OneToOneField('message.Message', verbose_name='id последнего сообщения чата',
                                        on_delete=models.SET_NULL, null=True, related_name='last_message_of_chat')
    # avatar = models.ImageField(upload_to='images/', null=True)

    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'


class Member (models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.SET_NULL, null=True,
                             related_name='members')
    chat = models.ForeignKey(Chat, verbose_name='чат', on_delete=models.SET_NULL, null=True, related_name='members')
    new_messages = models.IntegerField(verbose_name="количество непрочитанных сообщений в конкретном чате", default=0)
    last_read_message = models.ForeignKey('message.Message', verbose_name='последнее сообщение чата',
                                          on_delete=models.SET_NULL, null=True, related_name='members')

    class Meta:
        verbose_name = 'участник чата'
        verbose_name_plural = 'участники чата'

