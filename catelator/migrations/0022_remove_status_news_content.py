# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0021_status_news_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='news_content',
        ),
    ]
