# Generated by Django 4.0.3 on 2022-04-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_player_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
