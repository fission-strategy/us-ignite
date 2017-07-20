

from django.apps import AppConfig
from watson import search as watson


class ReversePitchConfig(AppConfig):
    name = 'us_ignite.smart_gigabit_communities'

    def ready(self):
        Pitch = self.get_model("Pitch")
        watson.register(Pitch.objects.filter(active=True))
