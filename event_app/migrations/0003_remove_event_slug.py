# Generated by Django 2.2 on 2020-12-02 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0002_event_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
