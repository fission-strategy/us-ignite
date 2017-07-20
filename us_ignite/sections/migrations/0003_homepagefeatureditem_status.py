# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 05:12


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_auto_20170202_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagefeatureditem',
            name='status',
            field=models.IntegerField(choices=[(1, 'Published'), (2, 'Draft'), (3, 'Removed')], default=2),
        ),
    ]
