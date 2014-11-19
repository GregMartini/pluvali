# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=30)),
                ('points', models.IntegerField(default=0)),
                ('fav_bg', models.IntegerField(default=90)),
                ('fav_text', models.IntegerField(default=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem', models.CharField(default='The Problem.', max_length=225)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('sceneID', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(default='Scenario Title', max_length=15)),
                ('description', models.CharField(default='Scenatio Decription', max_length=250)),
                ('problems', models.ForeignKey(to='CopingGame.Problems')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solution', models.CharField(default='Solution', max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('itemKey', models.AutoField(serialize=False, primary_key=True)),
                ('category', models.CharField(default='Themes', max_length=20)),
                ('itemName', models.CharField(default='ItemName', max_length=15)),
                ('itemDesc', models.CharField(default='Item Description', max_length=50)),
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
            model_name='purchases',
            name='itemFKey',
            field=models.ForeignKey(to='CopingGame.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchases',
            name='player',
            field=models.ForeignKey(to='CopingGame.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='problems',
            name='solutions',
            field=models.ManyToManyField(through='CopingGame.Scenario', to='CopingGame.Solutions'),
            preserve_default=True,
        ),
    ]
