# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 08:04


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_usercategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provile_category', to='profiles.UserCategory', verbose_name='Category I associate the most with'),
        ),
    ]
