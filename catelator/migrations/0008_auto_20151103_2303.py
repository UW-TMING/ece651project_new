# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0007_auto_20151102_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.CharField(default=b'static/upload/images/default.jpg', max_length=100),
        ),
    ]
