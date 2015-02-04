# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0012_auto_20150203_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='points',
            new_name='tokens',
        ),
    ]
