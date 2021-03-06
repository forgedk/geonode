# Generated by Django 2.2.20 on 2021-05-06 08:36

from django.db import migrations, models
import django.db.models.deletion
from django.db.models.fields.json import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0029_delete_mapsnapshot'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blob', JSONField(default=dict)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Map')),
            ],
        ),
        migrations.AddField(
            model_name='map',
            name='data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data', to='maps.MapData'),
        ),
    ]
