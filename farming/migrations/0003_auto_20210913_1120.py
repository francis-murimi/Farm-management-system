# Generated by Django 3.1.1 on 2021-09-13 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0002_farm_name'),
        ('farming', '0002_auto_20210913_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_harvest',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farm.animal'),
        ),
    ]
