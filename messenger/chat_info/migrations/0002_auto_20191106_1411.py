# Generated by Django 2.2.5 on 2019-11-06 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': 'прикрепление', 'verbose_name_plural': 'прикрипления'},
        ),
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'чат', 'verbose_name_plural': 'чаты'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'участник', 'verbose_name_plural': 'участники'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
    ]