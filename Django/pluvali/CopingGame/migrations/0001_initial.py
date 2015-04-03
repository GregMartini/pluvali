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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30)),
                ('tokens', models.IntegerField(default=0)),
                ('avatarPic', models.ImageField(upload_to='userPic/', default='userPic/default-user.png')),
                ('fav_bg', models.CharField(default='#ededed', max_length=30)),
                ('fav_text', models.CharField(default='black', max_length=30)),
                ('text_size', models.IntegerField(default=6)),
                ('stage', models.IntegerField(default=0)),
                ('temp_tokens', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pictureP', models.ImageField(upload_to='problems/', null=True)),
                ('problem', models.CharField(default='The Problem.', max_length=225)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('owned', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('sceneID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Scenario Title', max_length=35)),
                ('description', models.CharField(default='Scenatio Decription', max_length=250)),
                ('player_list', models.ManyToManyField(to='CopingGame.Player', blank=True)),
                ('problems', models.ManyToManyField(to='CopingGame.Problems')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pictureS', models.ImageField(upload_to='solutions/', null=True, blank=True)),
                ('solution', models.CharField(default='Solution', max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('itemKey', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(default='Themes', max_length=20)),
                ('itemName', models.CharField(default='ItemName', max_length=15)),
                ('itemDesc', models.CharField(default='Item Description', max_length=50)),
                ('itemPicture', models.ImageField(upload_to='store/', null=True, blank=True)),
                ('value1', models.CharField(blank=True, max_length=10)),
                ('value2', models.CharField(blank=True, max_length=10)),
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
