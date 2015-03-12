# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0019_auto_20150312_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='itemDesc',
            field=models.CharField(default='Item Description', max_length=50),
            preserve_default=True,
        ),
    ]
