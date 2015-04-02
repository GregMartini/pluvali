# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0029_player_temp_tokens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('groupName', models.CharField(default="Admin's Group", max_length=35)),
                ('player', models.ManyToManyField(to='CopingGame.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='scenario',
            name='group_list',
            field=models.ManyToManyField(to='CopingGame.Group'),
            preserve_default=True,
        ),
    ]
