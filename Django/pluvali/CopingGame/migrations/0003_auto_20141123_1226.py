# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0002_player_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='pictureP',
            field=models.ImageField(blank=True, null=True, upload_to='/media/problems/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='solutions',
            name='pictureS',
            field=models.ImageField(blank=True, null=True, upload_to='/media/solutions/'),
            preserve_default=True,
        ),
    ]
