# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0016_auto_20151203_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='pieshow',
            name='percent1',
            field=models.FloatField(default=0, max_length=100),
        ),
    ]
