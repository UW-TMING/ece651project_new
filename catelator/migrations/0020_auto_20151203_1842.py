# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0019_auto_20151203_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='columnshow',
            old_name='calories',
            new_name='average_calories',
        ),
        migrations.AddField(
            model_name='columnshow',
            name='selected_calories',
            field=models.FloatField(default=0, max_length=100),
        ),
    ]
