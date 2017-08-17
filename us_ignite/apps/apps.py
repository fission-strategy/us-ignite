

from django.apps import AppConfig
from watson import search as watson


class AppsConfig(AppConfig):
    name = 'us_ignite.apps'

    def ready(self):
        Application = self.get_model("Application")
        watson.register(Application.objects.filter(status=1),
                        store=('sector__name', 'sector__slug', 'programs', 'program__name', 'program__slug', 'created', 'categories', 'funder_keywords'))
