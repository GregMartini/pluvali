# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0030_auto_20150402_1454'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='PlayerGroup',
        ),
        migrations.AlterField(
            model_name='scenario',
            name='group_list',
            field=models.ManyToManyField(to='CopingGame.PlayerGroup', blank=True),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='player_list',
            field=models.ManyToManyField(to='CopingGame.Player', blank=True),
        ),
    ]
