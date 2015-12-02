# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0002_auto_20151030_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='creator',
            field=models.ForeignKey(related_name='dcreator', to='catelator.User'),
        ),
    ]
