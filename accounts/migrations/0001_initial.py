# Generated by Django 3.1.1 on 2021-09-08 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
            ],
            options={
                'verbose_name': 'county',
                'verbose_name_plural': 'counties',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.county')),
            ],
            options={
                'verbose_name': 'ward',
                'verbose_name_plural': 'wards',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.IntegerField()),
                ('phone_number', models.CharField(max_length=10)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=0)),
                ('disability', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ward')),
            ],
        ),
    ]
