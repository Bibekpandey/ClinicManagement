# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20150327_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerictestfield',
            name='childRange',
            field=models.ForeignKey(blank=True, related_name='child_range', null=True, to='records.Range'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='numerictestfield',
            name='femaleRange',
            field=models.ForeignKey(blank=True, related_name='female_range', null=True, to='records.Range'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='reportDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 4, 41, 50, 639501)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 4, 41, 50, 638927)),
            preserve_default=True,
        ),
    ]
