# Generated by Django 3.1.1 on 2021-09-15 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farming', '0006_auto_20210915_1221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='missiona',
            options={'ordering': ['start_time'], 'verbose_name': 'Animal Kept', 'verbose_name_plural': 'Animals Kept'},
        ),
    ]