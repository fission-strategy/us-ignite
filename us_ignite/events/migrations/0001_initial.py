# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 21:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import geoposition.fields
import taggit.managers
import us_ignite.common.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actionclusters', '0002_auto_20170130_2159'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hubs', '0002_auto_20170130_2159'),
        ('organizations', '0003_auto_20170130_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name', unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='event name')),
                ('slug', us_ignite.common.fields.AutoUUIDField(blank=True, editable=False, unique=True)),
                ('status', models.IntegerField(choices=[(1, b'Published'), (2, b'Draft'), (3, b'Removed')], default=1)),
                ('image', models.ImageField(blank=True, help_text=b'Image suggested ratio: 3:2', upload_to=b'events')),
                ('description', models.TextField(verbose_name='short description')),
                ('start_datetime', models.DateTimeField(verbose_name='Start Date/Time')),
                ('end_datetime', models.DateTimeField(blank=True, null=True, verbose_name='End Date/Time')),
                ('timezone', models.CharField(choices=[('US/Alaska', 'US/Alaska'), ('US/Aleutian', 'US/Aleutian'), ('US/Arizona', 'US/Arizona'), ('US/Central', 'US/Central'), ('US/East-Indiana', 'US/East-Indiana'), ('US/Eastern', 'US/Eastern'), ('US/Hawaii', 'US/Hawaii'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('US/Michigan', 'US/Michigan'), ('US/Mountain', 'US/Mountain'), ('US/Pacific', 'US/Pacific'), ('US/Pacific-New', 'US/Pacific-New'), ('US/Samoa', 'US/Samoa')], default=b'US/Eastern', max_length=30)),
                ('address', models.TextField()),
                ('scope', models.IntegerField(choices=[(1, b'National'), (2, b'Regional'), (3, b'Global')], default=1)),
                ('audience_other', models.CharField(blank=True, max_length=200)),
                ('website', models.URLField(blank=True, help_text='Please enter a URL starting with http or https', max_length=500)),
                ('section', models.IntegerField(choices=[(1, 'Default'), (2, 'Global City Teams')], default=1, help_text='Section where this event will be listed. Default is the main section.')),
                ('tickets_url', models.URLField(blank=True, help_text='Please enter a URL starting with http or https', max_length=500, verbose_name='Tickets URL')),
                ('position', geoposition.fields.GeopositionField(blank=True, max_length=42)),
                ('is_ignite', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('actionclusters', models.ManyToManyField(blank=True, to='actionclusters.ActionCluster', verbose_name='communities')),
                ('audiences', models.ManyToManyField(blank=True, to='events.Audience')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.Organization', verbose_name='Organization')),
            ],
            options={
                'ordering': ('-is_featured', 'start_datetime'),
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name', unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='EventURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(help_text='Please enter a URL starting with http or https', max_length=500, verbose_name='URL')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='hubs',
            field=models.ManyToManyField(blank=True, to='hubs.Hub', verbose_name='communities'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
