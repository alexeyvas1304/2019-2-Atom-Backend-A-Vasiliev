# Generated by Django 2.2.5 on 2019-11-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191130_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=200, null=True, verbose_name='ссылка на аватарку'),
        ),
    ]
