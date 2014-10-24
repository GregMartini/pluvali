# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0002_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scenario',
            old_name='desctiption',
            new_name='description',
        ),
        migrations.AddField(
            model_name='scenario',
            name='solutions',
            field=models.CharField(max_length=300, default=' '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scenario',
            name='problems',
            field=models.CharField(max_length=500),
        ),
    ]
