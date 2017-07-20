import urlparse
from django.http import HttpResponsePermanentRedirect, HttpResponseGone
from django.conf import settings
from django.contrib.redirects.models import Redirect
from mezzanine.core.middleware import RedirectFallbackMiddleware
from mezzanine.utils.sites import current_site_id


class DoNotTrackMiddleware(object):

    def process_request(self, request):
        request.is_dnt = request.META.get('HTTP_DNT') == '1'


class URLRedirectMiddleware(object):
    """Redirects an invalid HOST URL to the expected domain."""

    def process_request(self, request):
        host = request.META.get('HTTP_HOST', '')
        parsed_url = urlparse.urlparse(settings.SITE_URL)
        if not settings.DEBUG and not host == parsed_url.netloc:
            new_url = settings.SITE_URL + request.path_info
            return HttpResponsePermanentRedirect(new_url)


class CustomRedirectFallbackMiddleware(RedirectFallbackMiddleware):

    def process_response(self, request, response):
        if response.status_code == 404:
            lookup = {
                "site_id": current_site_id(),
                "old_path": request.get_full_path(),
            }
            """ 
                        Seperate query parameters and url if full absolute path contains 
                        query parameters using python urlparse library       
                    """
            parsed_url = None
            if "?" in lookup['old_path']:
                parsed_url = urlparse.urlparse(lookup['old_path'])
                # Now full path contains no query parameters
                lookup['old_path'] = parsed_url.path

            try:
                redirect = Redirect.objects.get(**lookup)
            except Redirect.DoesNotExist:
                pass
            else:
                if not redirect.new_path:
                    response = HttpResponseGone()
                else:
                    response = HttpResponsePermanentRedirect(redirect.new_path)
        return response