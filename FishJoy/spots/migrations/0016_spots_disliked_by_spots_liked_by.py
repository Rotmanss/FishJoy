# Generated by Django 4.1.5 on 2023-03-05 11:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spots', '0015_baits_user_fish_user_spots_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='spots',
            name='disliked_by',
            field=models.ManyToManyField(blank=True, related_name='disliked_spots', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='spots',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_spots', to=settings.AUTH_USER_MODEL),
        ),
    ]
