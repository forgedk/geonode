# Generated by Django 1.11.25 on 2019-10-04 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0028_remove_service_last_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='created',
        ),
    ]
