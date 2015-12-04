# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0011_auto_20151128_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='catelator.User', null=True),
        ),
        migrations.AlterField(
            model_name='friends',
            name='befollow',
            field=models.ForeignKey(to='catelator.User', null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='user',
            field=models.ForeignKey(to='catelator.User', null=True),
        ),
    ]
