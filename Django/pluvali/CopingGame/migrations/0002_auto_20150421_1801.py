# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='value1',
            new_name='bg',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='value2',
            new_name='text',
        ),
    ]
