# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0003_auto_20141123_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='pictureP',
            field=models.ImageField(null=True, upload_to='', storage=django.core.files.storage.FileSystemStorage(location='/media/'), blank=True),
        ),
    ]
