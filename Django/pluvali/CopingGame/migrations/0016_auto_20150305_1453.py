# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0015_player_avatarpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='player_list',
            field=models.ManyToManyField(to='CopingGame.Player'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='avatarPic',
            field=models.ImageField(upload_to='userPic/', default='userPic/default-user.png'),
        ),
    ]
