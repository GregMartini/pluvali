# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0005_auto_20150504_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenario',
            name='description',
        ),
    ]
