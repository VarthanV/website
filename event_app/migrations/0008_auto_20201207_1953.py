# Generated by Django 2.2 on 2020-12-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0007_auto_20201207_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='points',
            field=models.TextField(blank=True, null=True),
        ),
    ]