from django import template

register = template.Library()

@register.filter(name='val_to_key')
def val_to_key(value, arg):
    return value.replace(arg, '')

register.filter('val_to_key', val_to_key)