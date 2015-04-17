# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0005_player_scenario_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='tokens_earned',
            field=models.CommaSeparatedIntegerField(max_length=5, default='0,0,0,0,0'),
            preserve_default=True,
        ),
    ]
