# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0002_auto_20150421_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('owned', models.BooleanField(default=False)),
                ('itemFKey', models.ForeignKey(to='CopingGame.Store')),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='itemFKey',
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='player',
        ),
        migrations.DeleteModel(
            name='Purchases',
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name_plural': 'StoreItems'},
        ),
    ]
