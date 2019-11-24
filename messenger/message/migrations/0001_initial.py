# Generated by Django 2.2.5 on 2019-11-21 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000, verbose_name='содержание сообщения')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')),
                ('chat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='chats.Chat', verbose_name='чат')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
    ]
