# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0024_remove_status_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='news_content',
            field=ckeditor.fields.RichTextField(default=0),
        ),
    ]
