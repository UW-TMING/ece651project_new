# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0006_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
