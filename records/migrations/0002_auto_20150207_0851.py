# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='isContinuation',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='numberOfVisits',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='report',
            field=models.ForeignKey(blank=True, to='records.Report'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='test',
            field=models.ForeignKey(blank=True, to='records.Test'),
            preserve_default=True,
        ),
    ]
