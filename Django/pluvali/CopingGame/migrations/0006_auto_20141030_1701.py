# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0005_auto_20141030_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problems',
            name='scnario',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='prob',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='sol',
        ),
        migrations.RemoveField(
            model_name='solutions',
            name='problems',
        ),
        migrations.AddField(
            model_name='scenario',
            name='probs',
            field=models.ManyToManyField(to='CopingGame.Problems'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenario',
            name='sols',
            field=models.ManyToManyField(to='CopingGame.Solutions'),
            preserve_default=True,
        ),
    ]
