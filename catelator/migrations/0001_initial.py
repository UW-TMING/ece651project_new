# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dish_name', models.CharField(max_length=20)),
                ('recipe', models.CharField(max_length=20, null=True)),
                ('composition', models.CharField(max_length=100, null=True)),
                ('creator', models.CharField(default=b'0', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Expectation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('span', models.IntegerField(default=b'0')),
                ('increment', models.FloatField(default=b'0', max_length=10)),
                ('consumption', models.FloatField(default=b'0', max_length=10)),
                ('intake', models.FloatField(default=b'0', max_length=10)),
                ('start_date', models.DateField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material_name', models.CharField(max_length=20)),
                ('calorie', models.FloatField(default=b'0', max_length=10)),
                ('protein', models.FloatField(default=b'0', max_length=10)),
                ('vitamin', models.FloatField(default=b'0', max_length=10)),
                ('carbohydrate', models.FloatField(default=b'0', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('intake', models.FloatField(default=b'0', max_length=10)),
                ('intake_date', models.DateField(default=None, max_length=20)),
                ('expectation', models.ForeignKey(to='catelator.Expectation')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(default=b'female', max_length=20)),
                ('weight', models.FloatField(default=b'0', max_length=10)),
                ('height', models.FloatField(default=b'0', max_length=10)),
                ('birth', models.DateField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='UserCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection_date', models.DateField(default=None)),
                ('dish', models.ForeignKey(to='catelator.Dish')),
                ('user', models.ForeignKey(to='catelator.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like_date', models.DateField(default=None)),
                ('dish', models.ForeignKey(to='catelator.Dish')),
                ('user', models.ForeignKey(to='catelator.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_date', models.DateField(default=None)),
                ('dish', models.ForeignKey(to='catelator.Dish')),
                ('user', models.ForeignKey(to='catelator.User')),
            ],
        ),
        migrations.AddField(
            model_name='expectation',
            name='period',
            field=models.ForeignKey(to='catelator.Period'),
        ),
        migrations.AddField(
            model_name='expectation',
            name='user',
            field=models.ForeignKey(to='catelator.User'),
        ),
        migrations.AddField(
            model_name='dish',
            name='collections',
            field=models.ManyToManyField(related_name='ucollect', through='catelator.UserCollection', to='catelator.User'),
        ),
        migrations.AddField(
            model_name='dish',
            name='likes',
            field=models.ManyToManyField(related_name='ulike', through='catelator.UserLike', to='catelator.User'),
        ),
        migrations.AddField(
            model_name='dish',
            name='orders',
            field=models.ManyToManyField(related_name='uorder', through='catelator.UserOrder', to='catelator.User'),
        ),
    ]
