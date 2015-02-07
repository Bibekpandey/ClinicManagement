# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20150207_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workinghour',
            old_name='thuresday',
            new_name='thursday',
        ),
    ]
