# Generated by Django 5.0.6 on 2024-07-05 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dice', '0002_rename_value_die_value1_die_value2'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Die',
            new_name='DiceRoll',
        ),
    ]
