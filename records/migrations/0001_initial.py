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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('value', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumericResult',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('value', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('person_ptr', models.OneToOneField(serialize=False, primary_key=True, to='records.Person', parent_link=True, auto_created=True)),
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
                ('person_ptr', models.OneToOneField(serialize=False, primary_key=True, to='records.Person', parent_link=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('reportDate', models.DateTimeField(default=datetime.datetime(2015, 3, 4, 14, 47, 2, 759407))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestField',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('testfield_ptr', models.OneToOneField(serialize=False, primary_key=True, to='records.TestField', parent_link=True, auto_created=True)),
                ('childRange', models.OneToOneField(related_name='child_range', to='records.Range')),
                ('femaleRange', models.OneToOneField(related_name='female_range', to='records.Range')),
                ('maleRange', models.OneToOneField(related_name='male_range', to='records.Range')),
            ],
            options={
            },
            bases=('records.testfield',),
        ),
        migrations.CreateModel(
            name='BooleanTestField',
            fields=[
                ('testfield_ptr', models.OneToOneField(serialize=False, primary_key=True, to='records.TestField', parent_link=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 3, 4, 14, 47, 2, 758796))),
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
