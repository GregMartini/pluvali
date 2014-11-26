# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import CopingGame.models


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0005_auto_20141123_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='pictureP',
            field=models.ImageField(blank=True, null=True, upload_to=CopingGame.models.upload_path_handler),
        ),
    ]
