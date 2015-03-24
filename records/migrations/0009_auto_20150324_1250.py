# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20150309_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='bill',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='numericresult',
            name='value',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='reportDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 12, 50, 26, 59136)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testfield',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 12, 50, 26, 58579)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='totalBill',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
