# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statusupvote',
            name='user_name',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
