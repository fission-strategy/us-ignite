# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 00:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actionclusters', '0007_auto_20170213_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actioncluster',
            name='_meta_title',
        ),
        migrations.RemoveField(
            model_name='actioncluster',
            name='description',
        ),
        migrations.RemoveField(
            model_name='actioncluster',
            name='gen_description',
        ),
        migrations.RemoveField(
            model_name='actioncluster',
            name='keywords_string',
        ),
        migrations.RemoveField(
            model_name='actioncluster',
            name='site',
        ),
        migrations.RemoveField(
            model_name='actioncluster',
            name='title',
        ),
    ]