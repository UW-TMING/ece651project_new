# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0026_auto_20151202_0532'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(default=b'static/upload/images/default.jpg', max_length=100)),
                ('status', models.ForeignKey(to='catelator.Status')),
            ],
        ),
    ]
