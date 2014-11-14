# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0007_auto_20141030_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutions',
            name='problems',
            field=models.ForeignKey(default=1, to='CopingGame.Problems'),
            preserve_default=False,
        ),
    ]
