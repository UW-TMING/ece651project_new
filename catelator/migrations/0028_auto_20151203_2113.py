# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0027_statuspicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuspicture',
            name='status',
            field=models.ForeignKey(to='catelator.Status', null=True),
        ),
    ]
