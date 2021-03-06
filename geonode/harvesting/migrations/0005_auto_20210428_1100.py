# Generated by Django 2.2.16 on 2021-04-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvesting', '0004_auto_20210428_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvester',
            name='remote_available',
            field=models.BooleanField(default=False, editable=False, help_text='Whether the remote service is known to be available or not'),
        ),
    ]
