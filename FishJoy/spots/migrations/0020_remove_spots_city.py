# Generated by Django 4.1.5 on 2023-04-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0019_spots_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spots',
            name='city',
        ),
    ]