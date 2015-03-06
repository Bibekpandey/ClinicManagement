# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooleanResult',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('value', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumericResult',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('value', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, to='records.Person', serialize=False)),
                ('numberOfVisits', models.IntegerField(default=1)),
                ('membership', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=('records.person',),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, to='records.Person', serialize=False)),
                ('hospital', models.CharField(max_length=50)),
                ('field', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=('records.person',),
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('startValue', models.IntegerField(default=0)),
                ('endValue', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('reportDate', models.DateTimeField(default=datetime.datetime(2015, 3, 6, 16, 47, 13, 993627))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestField',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumericTestField',
            fields=[
                ('testfield_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, to='records.TestField', serialize=False)),
                ('childRange', models.OneToOneField(to='records.Range', related_name='child_range')),
                ('femaleRange', models.OneToOneField(to='records.Range', related_name='female_range')),
                ('maleRange', models.OneToOneField(to='records.Range', related_name='male_range')),
            ],
            options={
            },
            bases=('records.testfield',),
        ),
        migrations.CreateModel(
            name='BooleanTestField',
            fields=[
                ('testfield_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, to='records.TestField', serialize=False)),
                ('positive', models.CharField(max_length=30)),
                ('negative', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=('records.testfield',),
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('comments', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 3, 6, 16, 47, 13, 992521))),
                ('totalBill', models.IntegerField(default=0)),
                ('comments', models.CharField(blank=True, max_length=100)),
                ('patient', models.ForeignKey(to='records.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testfield',
            name='testType',
            field=models.ForeignKey(to='records.TestType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='test',
            name='testType',
            field=models.ForeignKey(to='records.TestType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='test',
            name='visit',
            field=models.ForeignKey(to='records.Visit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='referredBy',
            field=models.OneToOneField(to='records.Doctor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numericresult',
            name='field',
            field=models.ForeignKey(to='records.NumericTestField'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numericresult',
            name='test',
            field=models.ForeignKey(to='records.Test'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booleanresult',
            name='field',
            field=models.ForeignKey(to='records.BooleanTestField'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booleanresult',
            name='test',
            field=models.ForeignKey(to='records.Test'),
            preserve_default=True,
        ),
    ]
