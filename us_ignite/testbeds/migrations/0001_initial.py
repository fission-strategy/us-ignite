# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 00:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import geoposition.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('organizations', '0003_auto_20170130_2159'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0011_auto_20170130_2159'),
        ('hubs', '0002_auto_20170130_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkSpeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testbed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of the Testbed')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name', unique=True)),
                ('summary', models.TextField(blank=True)),
                ('description', models.TextField()),
                ('website', models.URLField(blank=True, help_text='Please enter a URL starting with http or https', max_length=500)),
                ('image', models.ImageField(blank=True, max_length=500, upload_to=b'testbed')),
                ('connections', models.TextField(blank=True, verbose_name='Connections to other networks')),
                ('experimentation', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=2, verbose_name='Willingness to experiment')),
                ('passes_homes', models.PositiveIntegerField(default=0, verbose_name='Estimated passes # homes')),
                ('passes_business', models.PositiveIntegerField(default=0, verbose_name='Estimated passes # business')),
                ('passes_anchor', models.PositiveIntegerField(default=0, verbose_name='Estimated passes # community anchor')),
                ('is_advanced', models.BooleanField(default=False, help_text='Does it have advanced characteristics?')),
                ('position', geoposition.fields.GeopositionField(blank=True, max_length=42)),
                ('status', models.IntegerField(choices=[(1, 'Published'), (2, 'Draft')], default=2)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('applications', models.ManyToManyField(blank=True, to='apps.Application', verbose_name='Applications being piloted')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('features', models.ManyToManyField(blank=True, help_text='Existing NextGen features in this community.', to='apps.Feature')),
                ('hubs', models.ManyToManyField(blank=True, to='hubs.Hub', verbose_name='Communities')),
                ('network_speed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='testbeds.NetworkSpeed')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.Organization')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
