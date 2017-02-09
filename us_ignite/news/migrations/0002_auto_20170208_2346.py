# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170208_2345'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('blogpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.BlogPost')),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog')),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.blogpost',),
        ),
        migrations.RemoveField(
            model_name='news',
            name='blogpost_ptr',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
