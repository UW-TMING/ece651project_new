# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0017_pieshow_percent1'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnShow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(default=0, max_length=100)),
                ('calories', models.FloatField(default=0, max_length=100)),
            ],
        ),
    ]
