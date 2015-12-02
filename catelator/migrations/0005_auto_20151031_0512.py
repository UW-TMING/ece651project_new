# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0004_dish_status_quality'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='pic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='creator',
            field=models.ForeignKey(to='catelator.User'),
        ),
    ]
