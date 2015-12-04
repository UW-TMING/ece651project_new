# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0020_auto_20151203_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='reality',
            name='average_intake',
            field=models.FloatField(default=b'0', max_length=50),
        ),
    ]
