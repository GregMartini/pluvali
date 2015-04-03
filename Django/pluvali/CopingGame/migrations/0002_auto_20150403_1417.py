# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('groupName', models.CharField(max_length=35, default="Admin's Group")),
                ('player', models.ManyToManyField(to='CopingGame.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='scenario',
            name='group_list',
            field=models.ManyToManyField(to='CopingGame.PlayerGroup', blank=True),
            preserve_default=True,
        ),
    ]
