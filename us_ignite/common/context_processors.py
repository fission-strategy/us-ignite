from django.conf import settings

# MICROSITE_SLUGS = {
#     'globalcityteams': ['/globalcityteams/', '/actioncluster/'],
# }
#
# BASE_TEMPLATES = {
#     'globalcityteams': 'microsite_base.html',
# }


def get_site_slug(path):
    """Determines the prefix of the microsite if any."""
    # for key, item_list in MICROSITE_SLUGS.items():
    #     for item in item_list:
    #         if path.startswith(item):
    #             return key
    # return ''
    pass


def settings_available(request):
    slug = get_site_slug(request.path_info)
    # base_template = BASE_TEMPLATES[slug] if slug in BASE_TEMPLATES else 'base.html'
    base_template = 'base.html'
    return {
        'SITE_URL': settings.SITE_URL,
        'IS_PRODUCTION': settings.IS_PRODUCTION,
        # 'ACCOUNT_ACTIVATION_DAYS': settings.ACCOUNT_ACTIVATION_DAYS,
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
        'MICROSITE_SLUG': slug,
        'BASE_TEMPLATE': base_template,
    }
