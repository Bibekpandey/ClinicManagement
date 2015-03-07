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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('value', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
                ('field', models.CharField(max_length=40, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumericResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('value', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('person_ptr', models.OneToOneField(to='records.Person', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
                ('numberOfVisits', models.IntegerField(default=1)),
                ('membership', models.CharField(max_length=40)),
                ('referredBy', models.OneToOneField(to='records.Doctor', null=True)),
            ],
            options={
            },
            bases=('records.person',),
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('startValue', models.DecimalField(max_digits=7, decimal_places=5)),
                ('endValue', models.DecimalField(max_digits=7, decimal_places=5)),
                ('unit', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('reportDate', models.DateTimeField(default=datetime.datetime(2015, 3, 7, 3, 13, 17, 73919))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('testfield_ptr', models.OneToOneField(to='records.TestField', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
                ('childRange', models.ForeignKey(to='records.Range', blank=True, related_name='child_range')),
                ('femaleRange', models.ForeignKey(to='records.Range', null=True, related_name='female_range')),
                ('maleRange', models.ForeignKey(to='records.Range', related_name='male_range')),
            ],
            options={
            },
            bases=('records.testfield',),
        ),
        migrations.CreateModel(
            name='BooleanTestField',
            fields=[
                ('testfield_ptr', models.OneToOneField(to='records.TestField', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('comments', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 3, 7, 3, 13, 17, 73409))),
                ('totalBill', models.IntegerField(default=0)),
                ('comments', models.CharField(max_length=100, blank=True)),
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
