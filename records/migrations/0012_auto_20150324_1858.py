# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_auto_20150324_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='reportDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 18, 58, 18, 538038)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 18, 58, 18, 537472)),
            preserve_default=True,
        ),
    ]
