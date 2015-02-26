# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0014_auto_20150210_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='avatarPic',
            field=models.ImageField(null=True, blank=True, upload_to='userPic/'),
            preserve_default=True,
        ),
    ]
