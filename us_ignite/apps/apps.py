from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class AppsConfig(AppConfig):
    name = 'us_ignite.apps'

    def ready(self):
        Application = self.get_model("Application")
        watson.register(Application.objects.filter(status=Application.PUBLISHED),
                        store=('sector__name', 'sector__slug', 'program__name', 'program__slug', 'created', 'categories', 'funder_keywords'))
