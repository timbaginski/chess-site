# Generated by Django 4.1.4 on 2023-01-02 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_game_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='fen',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='game',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 15, 4, 12, 418229)),
        ),
    ]
