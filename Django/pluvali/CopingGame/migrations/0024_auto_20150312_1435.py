# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0023_auto_20150312_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='itemPicture',
            field=models.ImageField(upload_to='store/', blank=True),
        ),
    ]
