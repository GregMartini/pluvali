# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0021_auto_20150312_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='itemPicture',
            field=models.ImageField(null=True, blank=True, upload_to='store/'),
        ),
    ]
