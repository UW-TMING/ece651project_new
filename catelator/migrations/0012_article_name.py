# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0011_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.CharField(default=b'123', max_length=50),
        ),
    ]
