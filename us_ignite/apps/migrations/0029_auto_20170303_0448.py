# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 04:48


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20170303_0448'),
        ('news', '0014_auto_20170303_0448'),
        ('apps', '0028_auto_20170301_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='program',
            field=models.ForeignKey(blank=True, help_text='Does this application belong to any specific program?', null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.Program'),
        ),
        migrations.AlterField(
            model_name='applicationversion',
            name='program',
            field=models.ForeignKey(blank=True, help_text='Does this application belong to any specific program?', null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.Program'),
        ),
        migrations.DeleteModel(
            name='Program',
        ),
    ]
