# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0008_auto_20151103_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('follow', models.IntegerField(default=0)),
                ('befollow', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_content', models.CharField(max_length=255)),
                ('status_date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(to='catelator.User')),
            ],
        ),
        migrations.CreateModel(
            name='StatusUpvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('upvote_date', models.DateField(auto_now=True)),
                ('status', models.ForeignKey(to='catelator.Status')),
            ],
        ),
    ]
