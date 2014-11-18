# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('problem', models.CharField(max_length=225, default='The Problem.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaveState',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('sceneID', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=15, default='Scenario Title')),
                ('description', models.CharField(max_length=250, default='Scenatio Decription')),
                ('problems', models.ForeignKey(to='CopingGame.Problems')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('solution', models.CharField(max_length=300, default='Solution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('itemKey', models.AutoField(serialize=False, primary_key=True)),
                ('itemName', models.CharField(max_length=15, default='ItemName')),
                ('itemDesc', models.CharField(max_length=50, default='Item Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(serialize=False, primary_key=True)),
                ('userName', models.CharField(max_length=12, default='User')),
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
            model_name='scenario',
            name='solutions',
            field=models.ForeignKey(to='CopingGame.Solutions'),
            preserve_default=True,
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
        migrations.AddField(
            model_name='problems',
            name='solutions',
            field=models.ManyToManyField(to='CopingGame.Solutions', through='CopingGame.Scenario'),
            preserve_default=True,
        ),
    ]
