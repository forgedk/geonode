# Generated by Django 1.11.11 on 2018-04-09 12:38


from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0030_auto_20180302_0430'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='document',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
