# Generated by Django 4.2 on 2023-05-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Growth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pop2023', models.IntegerField()),
                ('pop2022', models.IntegerField()),
                ('city', models.TextField()),
                ('country', models.TextField()),
                ('growthrate', models.FloatField(db_column='growthRate')),
                ('type', models.TextField()),
                ('rank', models.IntegerField()),
                ('state', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'growth',
            },
        ),
        migrations.CreateModel(
            name='MetroSystems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField()),
                ('country_region', models.TextField()),
                ('name', models.TextField()),
                ('service_opened', models.IntegerField()),
                ('last_expanded', models.IntegerField()),
                ('stations', models.IntegerField()),
                ('system_length', models.FloatField()),
                ('annual_ridership', models.FloatField(blank=True, null=True)),
                ('rail_type', models.TextField()),
            ],
            options={
                'db_table': 'metro_systems',
            },
        ),
        migrations.CreateModel(
            name='UsCityClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('state', models.TextField()),
                ('population', models.IntegerField()),
                ('area', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('population_density', models.FloatField()),
                ('growth_rate', models.FloatField()),
                ('rail_type', models.TextField()),
            ],
            options={
                'db_table': 'us_city_class',
            },
        ),
        migrations.CreateModel(
            name='WorldCityClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('name2', models.TextField()),
                ('country', models.TextField()),
                ('population', models.IntegerField()),
                ('area', models.FloatField()),
                ('countrycode', models.TextField(db_column='countryCode')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('population_density', models.FloatField()),
                ('growth_rate', models.FloatField()),
                ('rail_type', models.TextField()),
            ],
            options={
                'db_table': 'world_city_class',
            },
        ),
    ]
