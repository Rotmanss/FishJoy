# Generated by Django 4.1.5 on 2023-02-25 19:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0012_remove_fish_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='spots',
            name='dislikes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='spots',
            name='likes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
