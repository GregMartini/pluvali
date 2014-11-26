# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0006_auto_20141125_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='fav_bg',
            field=models.CharField(max_length=30, default='#ededed'),
        ),
        migrations.AlterField(
            model_name='player',
            name='fav_text',
            field=models.CharField(max_length=30, default='black'),
        ),
    ]
