# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 00:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_remove_application_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='category_tags',
        ),
    ]
