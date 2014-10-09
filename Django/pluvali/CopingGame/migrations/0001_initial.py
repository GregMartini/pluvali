# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('uiColor', models.IntegerField(default=90)),
                ('fontColor', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('sceneID', models.AutoField(primary_key=True, serialize=False)),
                ('desctiption', models.CharField(max_length=250)),
                ('problems', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('points', models.IntegerField(default=0)),
                ('privileges', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='savestate',
            name='sceneIDfKey',
            field=models.ForeignKey(to='CopingGame.Scenario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='savestate',
            name='userIDfKey',
            field=models.ForeignKey(to='CopingGame.User'),
            preserve_default=True,
        ),
    ]
