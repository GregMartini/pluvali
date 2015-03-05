# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0016_auto_20150305_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenario',
            name='title',
            field=models.CharField(default='Scenario Title', max_length=35),
        ),
    ]
