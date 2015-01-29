# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0005_auto_20150128_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='pictureP',
            field=models.ImageField(upload_to='problems', null=True),
        ),
    ]
