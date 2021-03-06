# Generated by Django 2.2.16 on 2021-05-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvesting', '0013_auto_20210520_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvester',
            name='status',
            field=models.CharField(choices=[('ready', 'ready'), ('updating-harvestable-resources', 'updating-harvestable-resources'), ('harvesting-resources', 'harvesting-resources'), ('checking-availability', 'checking-availability')], default='ready', max_length=50),
        ),
    ]
