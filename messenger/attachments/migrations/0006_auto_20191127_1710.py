# Generated by Django 2.2.5 on 2019-11-27 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0005_attachment_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='avatar',
            new_name='data',
        ),
    ]
