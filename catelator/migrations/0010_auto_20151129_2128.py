# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0009_monthlyweatherbycity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reality',
            name='intake_date',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
