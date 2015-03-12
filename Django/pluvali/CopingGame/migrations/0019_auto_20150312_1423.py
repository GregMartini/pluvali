# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0018_auto_20150312_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='itemDesc',
        ),
        migrations.AddField(
            model_name='store',
            name='itemPicture',
            field=models.ImageField(upload_to='store/', null=True),
            preserve_default=True,
        ),
    ]
