# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0026_auto_20150312_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='owned',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
