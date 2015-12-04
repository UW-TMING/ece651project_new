# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0013_auto_20151202_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWeather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('temperature', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
                ('city', models.CharField(default=0, max_length=50)),
                ('state', models.CharField(default=0, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyWeatherSeattle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.IntegerField()),
                ('seattle_temp', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
            ],
        ),
        migrations.AddField(
            model_name='monthlyweatherbycity',
            name='new_york_temp',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=1),
        ),
        migrations.AddField(
            model_name='monthlyweatherbycity',
            name='san_franciso_temp',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='monthlyweatherbycity',
            name='boston_temp',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='monthlyweatherbycity',
            name='houston_temp',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=1),
        ),
    ]
