# Generated by Django 3.0.5 on 2020-06-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountriesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField()),
                ('today_deaths', models.IntegerField(null=True)),
                ('today_confirmed', models.IntegerField(null=True)),
                ('total_deaths', models.IntegerField(null=True)),
                ('total_confirmed', models.IntegerField(null=True)),
                ('total_recovered', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountriesName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country_pic', models.CharField(max_length=200)),
                ('alpha3Code', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.IntegerField(null=True)),
                ('confirmed', models.IntegerField(null=True)),
                ('deaths', models.IntegerField(null=True)),
                ('state', models.CharField(max_length=200)),
                ('updated_on', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorldData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worlddata_updated_at', models.DateTimeField()),
                ('worlddata_today_deaths', models.IntegerField(null=True)),
                ('worlddata_today_confirmed', models.IntegerField(null=True)),
                ('worlddata_today_recovered', models.IntegerField(null=True)),
                ('worlddata_total_deaths', models.IntegerField(null=True)),
                ('worlddata_total_confirmed', models.IntegerField(null=True)),
                ('worlddata_total_recovered', models.IntegerField(null=True)),
            ],
        ),
    ]
