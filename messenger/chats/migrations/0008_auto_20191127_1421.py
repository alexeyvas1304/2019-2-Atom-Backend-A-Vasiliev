# Generated by Django 2.2.5 on 2019-11-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0007_auto_20191127_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]