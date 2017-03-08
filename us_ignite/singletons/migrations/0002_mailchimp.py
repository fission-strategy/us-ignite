# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singletons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailChimp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(blank=True, max_length=100)),
                ('main_list', models.CharField(blank=True, max_length=100, verbose_name=b'Main Mailing List')),
            ],
        ),
    ]
