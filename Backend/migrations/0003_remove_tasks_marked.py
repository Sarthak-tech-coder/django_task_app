# Generated by Django 3.1.4 on 2021-04-01 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_auto_20210401_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='Marked',
        ),
    ]
