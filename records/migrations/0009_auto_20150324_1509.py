# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20150309_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabStaff',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReceptionStaff',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 15, 9, 7, 29206)),
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
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 15, 9, 7, 28633)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visit',
            name='totalBill',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
