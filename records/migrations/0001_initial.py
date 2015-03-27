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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('value', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
                ('field', models.CharField(blank=True, max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LabStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumericResult',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('value', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('person_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='records.Person')),
                ('numberOfVisits', models.IntegerField(default=1)),
                ('membership', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=('records.person',),
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('startValue', models.DecimalField(max_digits=12, decimal_places=5)),
                ('endValue', models.DecimalField(max_digits=12, decimal_places=5)),
                ('unit', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReceptionStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('reportOut', models.BooleanField(default=False)),
                ('reportDate', models.DateTimeField(default=datetime.datetime(2015, 3, 27, 3, 13, 41, 53292))),
                ('testDone', models.BooleanField(default=False)),
                ('bill', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestField',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumericTestField',
            fields=[
                ('testfield_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='records.TestField')),
                ('childRange', models.ForeignKey(related_name='child_range', blank=True, to='records.Range')),
                ('femaleRange', models.ForeignKey(to='records.Range', related_name='female_range', null=True)),
                ('maleRange', models.ForeignKey(related_name='male_range', to='records.Range')),
            ],
            options={
            },
            bases=('records.testfield',),
        ),
        migrations.CreateModel(
            name='BooleanTestField',
            fields=[
                ('testfield_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='records.TestField')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('comments', models.CharField(blank=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 3, 27, 3, 13, 41, 52718))),
                ('totalBill', models.FloatField(default=0)),
                ('comments', models.CharField(blank=True, max_length=100)),
                ('patient', models.ForeignKey(to='records.Patient')),
                ('referredBy', models.ForeignKey(to='records.Doctor', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testfield',
            name='category',
            field=models.ForeignKey(to='records.Category', blank=True, null=True),
            preserve_default=True,
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
            model_name='category',
            name='testType',
            field=models.ForeignKey(to='records.TestType', null=True),
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
