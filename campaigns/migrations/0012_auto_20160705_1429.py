# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0011_auto_20160626_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='last_active_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='entry_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='session_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='usergame',
            name='exp_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usergame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='campaigns.Game'),
        ),
        migrations.AlterField(
            model_name='usergame',
            name='last_active_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
