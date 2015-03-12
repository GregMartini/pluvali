# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0017_auto_20150305_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='value1',
            field=models.CharField(max_length=10, default='0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='value2',
            field=models.CharField(max_length=10, default='1'),
            preserve_default=True,
        ),
    ]
