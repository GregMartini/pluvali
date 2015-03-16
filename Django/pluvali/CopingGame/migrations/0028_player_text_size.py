# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0027_purchases_owned'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='text_size',
            field=models.IntegerField(default=6),
            preserve_default=True,
        ),
    ]
