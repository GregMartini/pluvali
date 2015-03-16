# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0028_player_text_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='temp_tokens',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
