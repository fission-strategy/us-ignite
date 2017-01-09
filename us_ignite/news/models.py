from __future__ import unicode_literals

from django.db import models
from mezzanine.blog.models import BlogPost

# Create your models here.


class News(BlogPost):
    excerpt = models.TextField(blank=True, default='')
