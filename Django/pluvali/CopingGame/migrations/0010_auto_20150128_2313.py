# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0009_auto_20150128_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='pictureP',
            field=models.ImageField(upload_to='/media/problems/', null=True),
        ),
        migrations.AlterField(
            model_name='solutions',
            name='pictureS',
            field=models.ImageField(upload_to='/media/solutions/', blank=True, null=True),
        ),
    ]
