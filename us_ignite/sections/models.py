from __future__ import unicode_literals

from django.db import models

# Create your models here.


class HomepageFeaturedItem(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    REMOVED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (REMOVED, 'Removed'),
    )

    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    class Meta(object):
        ordering = ('order', )


class HomepageProgram(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    REMOVED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (REMOVED, 'Removed'),
    )

    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    class Meta(object):
        ordering = ('order', )
