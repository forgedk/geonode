# Generated by Django 3.2.4 on 2021-06-24 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('harvesting', '0023_harvestableresource_last_refreshed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='harvestableresource',
            name='available',
        ),
    ]
