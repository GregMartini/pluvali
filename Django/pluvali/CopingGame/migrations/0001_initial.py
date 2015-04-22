# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('groupName', models.CharField(default="Admin's Group", max_length=35)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('pictureP', models.ImageField(upload_to='problems/', null=True)),
                ('problem', models.CharField(default='The Problem.', max_length=225)),
                ('pVideoId', models.CharField(default='q_g7s2oBzCw', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('group_list', models.ManyToManyField(to='CopingGame.PlayerGroup', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('pictureS', models.ImageField(upload_to='solutions/', blank=True, null=True)),
                ('solution', models.CharField(default='Solution', max_length=300)),
                ('sVideoId', models.CharField(default='q_g7s2oBzCw', max_length=50)),
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
                ('itemPicture', models.ImageField(upload_to='store/', blank=True, null=True)),
                ('value1', models.CharField(blank=True, max_length=10)),
                ('value2', models.CharField(blank=True, max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], verbose_name='username', unique=True, max_length=30)),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=75)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('tokens', models.IntegerField(default=0)),
                ('avatarPic', models.ImageField(upload_to='userPic/', default='userPic/default-user.png')),
                ('fav_bg', models.CharField(default='#ededed', max_length=30)),
                ('fav_text', models.CharField(default='black', max_length=30)),
                ('text_size', models.IntegerField(default=6)),
                ('stage', models.IntegerField(default=0)),
                ('scenario_tokens', models.IntegerField(default=0)),
                ('tokens_earned', models.CharField(default='0,0,0,0,0', max_length=9)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set', to='auth.Group', related_query_name='user', verbose_name='groups', blank=True)),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', related_name='user_set', to='auth.Permission', related_query_name='user', verbose_name='user permissions', blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='scenario',
            name='player_list',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenario',
            name='problems',
            field=models.ManyToManyField(to='CopingGame.Problems'),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='problems',
            name='solutions',
            field=models.ManyToManyField(to='CopingGame.Solutions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playergroup',
            name='player',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
