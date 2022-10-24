# Generated by Django 3.2.6 on 2022-10-24 18:03

import blango_auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blango_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', blango_auth.models.BlangoUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
