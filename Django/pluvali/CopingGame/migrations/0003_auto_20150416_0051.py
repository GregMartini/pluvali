# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0002_auto_20150403_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='videoId',
            field=models.CharField(default='q_g7s2oBzCw', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='solutions',
            name='videoId',
            field=models.CharField(default='q_g7s2oBzCw', max_length=50),
            preserve_default=True,
        ),
    ]
