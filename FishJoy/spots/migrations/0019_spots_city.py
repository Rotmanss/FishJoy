# Generated by Django 4.1.5 on 2023-04-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0018_alter_feedback_options_alter_feedback_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='spots',
            name='city',
            field=models.CharField(default='Kyiv', max_length=50),
            preserve_default=False,
        ),
    ]
