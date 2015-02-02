# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('middleName', models.CharField(max_length=30, blank=True)),
                ('lastName', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='records.Person', serialize=False, parent_link=True)),
                ('bloodGroup', models.CharField(max_length=5)),
                ('firstVisit', models.DateTimeField()),
                ('numberOfVisits', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=('records.person',),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='records.Person', serialize=False, parent_link=True)),
                ('dateJoined', models.DateTimeField()),
                ('qualification', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=('records.person',),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='records.Person', serialize=False, parent_link=True)),
                ('dateJoined', models.DateTimeField()),
                ('qualification', models.CharField(max_length=100)),
                ('workingField', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=('records.person',),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('testType', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('isClear', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('isFirstVisit', models.BooleanField(default=False)),
                ('isFollowup', models.BooleanField(default=False)),
                ('patientProblems', models.CharField(max_length=200)),
                ('problems', models.CharField(max_length=500)),
                ('appointmentTime', models.DateTimeField()),
                ('appointmentDoc', models.ForeignKey(to='records.Doctor')),
                ('medicine', models.ManyToManyField(to='records.Medicine', blank=True)),
                ('patient', models.ForeignKey(to='records.Patient')),
                ('report', models.ForeignKey(to='records.Report')),
                ('test', models.ForeignKey(to='records.Test')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='report',
            name='test',
            field=models.ForeignKey(to='records.Test'),
            preserve_default=True,
        ),
    ]
