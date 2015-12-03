# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0018_columnshow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='columnshow',
            old_name='content',
            new_name='c_name',
        ),
    ]
