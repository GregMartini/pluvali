# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0025_remove_store_itempicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='itemPicture',
            field=models.ImageField(upload_to='store/', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='value1',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='value2',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
