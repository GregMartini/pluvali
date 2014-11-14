# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0003_auto_20141023_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='title',
            field=models.CharField(max_length=15, default='Scenario Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='itemName',
            field=models.CharField(max_length=15, default='ItemName'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scenario',
            name='description',
            field=models.CharField(max_length=250, default='Scenatio Decription'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='problems',
            field=models.CharField(max_length=500, default='Problem'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='solutions',
            field=models.CharField(max_length=300, default='Solution'),
        ),
        migrations.AlterField(
            model_name='store',
            name='itemDesc',
            field=models.CharField(max_length=50, default='Item Description'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=12, default='User'),
        ),
    ]
