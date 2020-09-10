# Generated by Django 3.0.8 on 2020-09-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0006_schedule_original_winner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifier_type', models.TextField()),
                ('team1', models.TextField()),
                ('team2', models.TextField()),
                ('date', models.TextField()),
                ('time', models.TextField()),
                ('city', models.TextField()),
                ('predicted_winner', models.TextField()),
                ('original_winner', models.TextField()),
            ],
        ),
    ]