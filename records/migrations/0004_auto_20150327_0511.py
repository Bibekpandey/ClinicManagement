# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20150327_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerictestfield',
            name='maleRange',
            field=models.ForeignKey(to='records.Range', related_name='male_range', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='reportDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 5, 11, 37, 558165)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 5, 11, 37, 557522)),
            preserve_default=True,
        ),
    ]
