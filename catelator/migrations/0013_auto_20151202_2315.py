# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelator', '0012_article_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('select', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='dish',
            name='composition',
        ),
        migrations.AddField(
            model_name='dish',
            name='calories',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='dish',
            name='carbohydrates',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='dish',
            name='protein',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='dish',
            name='vitamins',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='dish',
            field=models.ForeignKey(to='catelator.Dish'),
        ),
    ]
