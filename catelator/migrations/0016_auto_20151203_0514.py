# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0015_pieshow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieshow',
            name='percent',
            field=models.FloatField(default=0, max_length=100),
        ),
    ]
