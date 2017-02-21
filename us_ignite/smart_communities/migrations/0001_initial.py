# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FundingPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('image', mezzanine.core.fields.FileField(max_length=255, verbose_name='File')),
                ('link', models.URLField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(2, 'Published'), (1, 'Draft'), (3, 'Removed')], default=1)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
