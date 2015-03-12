# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0020_store_itemdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='itemPicture',
            field=models.ImageField(blank=True, upload_to='store/'),
        ),
    ]
