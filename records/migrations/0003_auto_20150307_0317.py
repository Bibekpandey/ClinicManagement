# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20150307_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='range',
            name='endValue',
            field=models.DecimalField(max_digits=12, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='range',
            name='startValue',
            field=models.DecimalField(max_digits=12, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='reportDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 7, 3, 17, 34, 652276)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 7, 3, 17, 34, 651766)),
            preserve_default=True,
        ),
    ]
