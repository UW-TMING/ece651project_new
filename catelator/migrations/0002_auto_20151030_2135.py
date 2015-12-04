# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='recipe',
            field=models.TextField(null=True),
        ),
    ]
