# Generated by Django 3.1 on 2020-08-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0002_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='teams',
            new_name='team1',
        ),
        migrations.AddField(
            model_name='schedule',
            name='team2',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
