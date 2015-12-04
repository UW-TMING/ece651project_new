# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0014_auto_20151203_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='PieShow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(default=0, max_length=100)),
                ('percent', models.CharField(default=0, max_length=100)),
            ],
        ),
    ]
