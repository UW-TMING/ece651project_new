# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0028_auto_20151203_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status_date',
            field=models.DateField(),
        ),
    ]
