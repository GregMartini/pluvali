# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0003_auto_20150422_0212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problems',
            options={'verbose_name_plural': 'Problems'},
        ),
        migrations.AlterModelOptions(
            name='solutions',
            options={'verbose_name_plural': 'Solutions'},
        ),
    ]
