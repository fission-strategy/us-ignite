# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 05:02


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150527_1555'),
        ('profiles', '0004_auto_20170227_0011'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provile_category', to='blog.BlogCategory', verbose_name='I associate most with'),
        ),
        migrations.AddField(
            model_name='user',
            name='category_other',
            field=models.ManyToManyField(blank=True, related_name='profile_category_other', to='blog.BlogCategory', verbose_name='Other categories I associate with'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_public',
            field=models.BooleanField(default=False, help_text=b'By marking the profile as public it will be shown in search results.'),
        ),
    ]
