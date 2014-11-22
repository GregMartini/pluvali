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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('problem', models.CharField(max_length=225, default='The Problem.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('sceneID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=15, default='Scenario Title')),
                ('description', models.CharField(max_length=250, default='Scenatio Decription')),
                ('problems', models.ManyToManyField(to='CopingGame.Problems')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('solution', models.CharField(max_length=300, default='Solution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('itemKey', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20, default='Themes')),
                ('itemName', models.CharField(max_length=15, default='ItemName')),
                ('itemDesc', models.CharField(max_length=50, default='Item Description')),
            ],
            options={
            },
            bases=(models.Model,),
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
            field=models.ManyToManyField(to='CopingGame.Solutions'),
            preserve_default=True,
        ),
    ]
