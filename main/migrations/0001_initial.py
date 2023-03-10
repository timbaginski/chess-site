# Generated by Django 4.1.4 on 2022-12-24 23:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.BooleanField(default=False)),
                ('ended', models.BooleanField(default=False)),
                ('blackPlayers', models.ManyToManyField(blank=True, related_name='black_players', to=settings.AUTH_USER_MODEL)),
                ('whitePlayers', models.ManyToManyField(blank=True, related_name='white_players', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
