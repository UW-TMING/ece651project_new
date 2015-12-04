# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0003_auto_20151030_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='status_quality',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'during_approve'), (b'1', b'not_approved'), (b'2', b'approved')]),
        ),
    ]
