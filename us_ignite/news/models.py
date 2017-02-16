from __future__ import unicode_literals

from django.db import models
from mezzanine.blog.models import BlogPost
from mezzanine.utils.models import upload_to
from mezzanine.core.fields import FileField
from django.utils.translation import ugettext_lazy as _
from mezzanine.generic.fields import KeywordsField


class NewsPost(BlogPost):
    excerpt = models.TextField(blank=True, null=True)
    image = FileField(_("File"), max_length=255, format="Image",
        upload_to=upload_to("news.NewsPost.image", "galleries"), null=True, blank=True)
    categories_new = models.ManyToManyField("apps.Category", blank=True, verbose_name="Categories")
    program = models.ForeignKey('apps.Program', blank=True, null=True,
                                     help_text=_("Does this application belong to any specific program"))


class Link(models.Model):
    PUBLISHED = 1
    DRAFT = 2
    DELETED = 3
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (DELETED, 'Deleted'),
    )
    title = models.CharField(max_length=255)
    url = models.URLField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)


# class Image(GalleryImage):
#     gallery = models.ForeignKey("NewsPost", related_name="images")
