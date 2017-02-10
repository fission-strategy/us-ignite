from __future__ import unicode_literals

from django.db import models
from mezzanine.core.fields import FileField
from mezzanine.utils.models import upload_to
from django.utils.translation import ugettext_lazy as _


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


class Sponsor(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    REMOVED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (REMOVED, 'Removed'),
    )

    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    name = models.CharField(max_length=255)
    image = FileField(_("File"), max_length=255, format="Image",
        upload_to=upload_to("sections.Sponsor.image", "galleries"))
    link = models.URLField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
