# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20150306_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='referredBy',
            field=models.OneToOneField(null=True, to='records.Doctor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='reportDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 16, 52, 40, 257536)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 16, 52, 40, 256707)),
            preserve_default=True,
        ),
    ]
