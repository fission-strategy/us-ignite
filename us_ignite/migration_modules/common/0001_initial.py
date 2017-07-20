# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 22:54


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('status', models.IntegerField(choices=[(2, 'Published'), (1, 'Draft'), (3, 'Removed')], default=1)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_link_set', to='pages.RichTextPage')),
            ],
        ),
    ]
