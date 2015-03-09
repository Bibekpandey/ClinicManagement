# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_auto_20150309_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='referredBy',
        ),
        migrations.AddField(
            model_name='visit',
            name='referredBy',
            field=models.ForeignKey(to='records.Doctor', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='reportDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 4, 48, 20, 945661)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 4, 48, 20, 945096)),
            preserve_default=True,
        ),
    ]
