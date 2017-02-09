from __future__ import unicode_literals

from django.db import models
from mezzanine.blog.models import BlogPost

# Create your models here.


class NewsPost(BlogPost):
    excerpt = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='blog')
