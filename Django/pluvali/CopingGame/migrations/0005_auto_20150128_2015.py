# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0004_auto_20150128_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='pictureP',
            field=models.ImageField(null=True, upload_to='/problems/'),
        ),
    ]
