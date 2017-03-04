# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20170303_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='funding_agents',
        ),
        migrations.AddField(
            model_name='fundingpartner',
            name='program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programs.Program'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='status',
            field=models.IntegerField(choices=[(2, 'Published'), (1, 'Draft'), (3, 'Removed')], default=1),
        ),
    ]