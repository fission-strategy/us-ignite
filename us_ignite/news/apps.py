from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class NewsConfig(AppConfig):
    name = 'us_ignite.news'
    verbose_name = 'content'

    def ready(self):
        NewsPost = self.get_model("NewsPost")
        watson.register(NewsPost.objects.filter(status=2))

