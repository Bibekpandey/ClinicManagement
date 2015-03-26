# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20150326_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='testType',
            field=models.ForeignKey(null=True, to='records.TestType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='reportDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 16, 22, 33, 353550)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 16, 22, 33, 352662)),
            preserve_default=True,
        ),
    ]
