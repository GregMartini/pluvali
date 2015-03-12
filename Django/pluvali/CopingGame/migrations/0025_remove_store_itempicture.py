# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0024_auto_20150312_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='itemPicture',
        ),
    ]
