# Generated by Django 2.2.5 on 2019-11-21 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chats', '0001_initial'),
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attachments', to='chats.Chat', verbose_name='чат'),
        ),
    ]
