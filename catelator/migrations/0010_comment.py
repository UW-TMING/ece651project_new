# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0009_friends_status_statusupvote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_content', models.CharField(default=None, max_length=255)),
                ('content_date', models.DateField(auto_now=True)),
                ('user_id', models.IntegerField(default=0)),
                ('status', models.ForeignKey(to='catelator.Status')),
            ],
        ),
    ]
