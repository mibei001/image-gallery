# Generated by Django 4.0.4 on 2022-05-29 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='location',
        ),
    ]
