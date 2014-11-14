# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CopingGame', '0004_auto_20141023_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('problem', models.CharField(default='The Problem.', max_length=225)),
                ('scnario', models.ForeignKey(to='CopingGame.Scenario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('solution', models.CharField(default='Solution', max_length=300)),
                ('problems', models.ForeignKey(to='CopingGame.Problems')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='problems',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='solutions',
        ),
        migrations.AddField(
            model_name='scenario',
            name='prob',
            field=models.ManyToManyField(to='CopingGame.Problems'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenario',
            name='sol',
            field=models.ManyToManyField(to='CopingGame.Solutions'),
            preserve_default=True,
        ),
    ]
