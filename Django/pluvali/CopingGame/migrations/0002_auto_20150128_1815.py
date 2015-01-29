# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import CopingGame.models


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='stage',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='problems',
            name='pictureP',
            field=models.ImageField(null=True, upload_to=CopingGame.models.upload_path_handler),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='solutions',
            name='pictureS',
            field=models.ImageField(null=True, blank=True, upload_to='/media/solutions/'),
            preserve_default=True,
        ),
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
