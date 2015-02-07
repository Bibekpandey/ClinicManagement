# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20150207_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingHour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('sunday', models.CharField(max_length=20)),
                ('monday', models.CharField(max_length=20)),
                ('tuesday', models.CharField(max_length=20)),
                ('wednesday', models.CharField(max_length=20)),
                ('thuresday', models.CharField(max_length=20)),
                ('friday', models.CharField(max_length=20)),
                ('saturday', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='doctor',
            name='workingHour',
            field=models.OneToOneField(to='records.WorkingHour', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staff',
            name='workingHour',
            field=models.OneToOneField(to='records.WorkingHour', null=True),
            preserve_default=True,
        ),
    ]
