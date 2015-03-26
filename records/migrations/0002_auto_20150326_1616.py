# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='reportDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 16, 16, 23, 228035)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 16, 16, 23, 227007)),
            preserve_default=True,
        ),
    ]
