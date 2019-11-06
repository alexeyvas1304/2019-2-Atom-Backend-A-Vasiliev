# Generated by Django 2.2.5 on 2019-11-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0005_auto_20191106_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reg_date',
            field=models.DateTimeField(default='1970-01-01 12:00:00', verbose_name='дата регистрации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=100, verbose_name='ссылка на аватарку'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nick',
            field=models.CharField(max_length=50, verbose_name='ник'),
        ),
    ]