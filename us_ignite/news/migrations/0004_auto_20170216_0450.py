# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 04:50


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0025_merge_20170216_0058'),
        ('news', '0003_remove_newspost_category_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspost',
            name='category_keywords_string',
        ),
        migrations.AddField(
            model_name='newspost',
            name='categories_new',
            field=models.ManyToManyField(blank=True, to='apps.Category'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='program',
            field=models.ForeignKey(blank=True, help_text='Does this application belong to any specific program', null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.Program'),
        ),
    ]
