# Generated by Django 4.0.3 on 2022-04-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_player_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
    ]
