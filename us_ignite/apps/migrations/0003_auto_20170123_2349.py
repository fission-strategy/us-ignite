# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 23:49


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20170105_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
