# Generated by Django 4.0.3 on 2022-04-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
