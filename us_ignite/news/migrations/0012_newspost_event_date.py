# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 00:13


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_newspost_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='event_date',
            field=models.DateTimeField(blank=True, db_index=True, help_text='Event date', null=True, verbose_name='Event date'),
        ),
    ]
