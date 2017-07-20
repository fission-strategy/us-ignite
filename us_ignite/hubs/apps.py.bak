from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class HubsConfig(AppConfig):
    name = 'us_ignite.hubs'

    def ready(self):
        Hub = self.get_model("Hub")
        watson.register(Hub.objects.filter(status=Hub.PUBLISHED))
