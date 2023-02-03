# Generated by Django 4.1.5 on 2023-01-24 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0004_baits_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='baits',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baits',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fish',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fish',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
