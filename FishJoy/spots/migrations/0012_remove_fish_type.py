# Generated by Django 4.1.5 on 2023-01-28 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0011_alter_fish_average_weight_alter_spots_max_depth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='type',
        ),
    ]