# Generated by Django 4.1.7 on 2023-02-28 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Team',
        ),
    ]
