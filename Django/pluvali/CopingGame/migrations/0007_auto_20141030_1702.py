# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0006_auto_20141030_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scenario',
            old_name='probs',
            new_name='problems',
        ),
        migrations.RenameField(
            model_name='scenario',
            old_name='sols',
            new_name='solutions',
        ),
    ]
