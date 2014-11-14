# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0008_solutions_problems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenario',
            name='solutions',
        ),
        migrations.RemoveField(
            model_name='solutions',
            name='problems',
        ),
        migrations.AddField(
            model_name='problems',
            name='solutions',
            field=models.ManyToManyField(to='CopingGame.Solutions'),
            preserve_default=True,
        ),
    ]
