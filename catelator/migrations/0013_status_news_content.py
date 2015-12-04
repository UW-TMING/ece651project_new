# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0012_auto_20151201_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='news_content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
