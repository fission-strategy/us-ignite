from __future__ import unicode_literals

from django.db import models
from mezzanine.blog.models import BlogPost
from mezzanine.utils.models import upload_to
from mezzanine.core.fields import FileField
from django.utils.translation import ugettext_lazy as _
from mezzanine.generic.fields import KeywordsField


class NewsPost(BlogPost):
    is_featured = models.BooleanField(default=False)
    excerpt = models.TextField(blank=True, null=True)
    image = FileField(_("File"), max_length=255, format="Image",
        upload_to=upload_to("news.NewsPost.image", "galleries"), null=True, blank=True)
    program = models.ForeignKey('programs.Program', blank=True, null=True,
                                     help_text=_("Does this application belong to any specific program"))
    event = models.BooleanField(default=False, help_text="Is it an event?")

    event_date = models.DateTimeField(_("Event date"),
                                        help_text=_("Event date"),
                                        blank=True, null=True, db_index=True)

    def is_blog_post(self):
        return True


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
