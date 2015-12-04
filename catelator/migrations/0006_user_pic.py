# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0005_auto_20151031_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
