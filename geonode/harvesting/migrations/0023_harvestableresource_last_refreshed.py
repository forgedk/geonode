# Generated by Django 3.2.4 on 2021-06-24 00:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('harvesting', '0022_alter_harvester_default_access_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvestableresource',
            name='last_refreshed',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 0, 5, 26, 321641, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
