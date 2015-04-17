# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0006_player_tokens_earned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='temp_tokens',
        ),
        migrations.AlterField(
            model_name='player',
            name='tokens_earned',
            field=models.CharField(max_length=9, default='0,0,0,0,0'),
        ),
    ]
