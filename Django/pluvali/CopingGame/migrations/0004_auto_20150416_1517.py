# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0003_auto_20150416_0051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problems',
            old_name='videoId',
            new_name='pVideoId',
        ),
        migrations.RenameField(
            model_name='solutions',
            old_name='videoId',
            new_name='sVideoId',
        ),
    ]
