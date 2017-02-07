from django import template
from us_ignite.apps.models import Application, Sector

register = template.Library()


@register.filter
def val_to_key(value, sector, limit=3):
    sector_obj = Sector.objects.get(name=sector)
    try:
        return Application.objects.filter(status=Application.PUBLISHED, sector=sector_obj.id).all()[:limit]
    except Application.DoesNotExist:
        return {}
register.filter('val_to_key', val_to_key)
