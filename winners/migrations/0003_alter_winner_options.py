# Generated by Django 5.0.6 on 2024-07-16 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('winners', '0002_winner_game_alter_winner_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='winner',
            options={'ordering': ['game__id']},
        ),
    ]
