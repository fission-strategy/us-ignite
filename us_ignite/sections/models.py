from __future__ import unicode_literals

from django.db import models
from mezzanine.core.fields import FileField, OrderField
from mezzanine.utils.models import upload_to
from django.utils.translation import ugettext_lazy as _
from adminsortable.models import SortableMixin


class HomepageFeaturedItem(SortableMixin):
    DRAFT = 1
    PUBLISHED = 2
    REMOVED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (REMOVED, 'Removed'),
    )

    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    class Meta(object):
        ordering = ('order', )

    def __unicode__(self):
        return self.title


class HomepageProgram(SortableMixin):
    DRAFT = 1
    PUBLISHED = 2
    REMOVED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (REMOVED, 'Removed'),
    )

    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    class Meta(object):
        ordering = ('order', )

    def __unicode__(self):
        return self.title


class SponsorBase(SortableMixin):
    DRAFT = 1
    PUBLISHED = 2
    REMOVED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (REMOVED, 'Removed'),
    )

    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=255)
    image = FileField(_("File"), max_length=255, format="Image",
        upload_to=upload_to("sections.Sponsor.image", "galleries"))
    link = models.URLField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    class Meta(object):
        ordering = ('order', )
        abstract = True

    def __unicode__(self):
        return self.name


class Sponsor(SponsorBase):
    pass