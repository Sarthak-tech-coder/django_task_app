# Generated by Django 3.1.4 on 2021-04-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='Marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='Completed',
            field=models.BooleanField(default=True),
        ),
    ]
