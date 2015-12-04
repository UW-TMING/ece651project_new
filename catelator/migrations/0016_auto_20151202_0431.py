# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0015_auto_20151202_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='news_content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
