from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import RichTextField


class LinkResource(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    REMOVED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (REMOVED, 'Removed'),
    )
    page = models.ForeignKey('pages.RichTextPage', related_name='page_link_set')
    name = models.CharField(max_length=255)
    url = models.URLField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    def __unicode__(self):
        return self.name
