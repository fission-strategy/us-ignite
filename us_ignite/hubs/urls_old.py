from django.conf.urls import url
from . import views

from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('hub_list'),
                                    permanent=True)),
    url(r'^apply/$', RedirectView.as_view(url=reverse_lazy('hub_application'),
                                          permanent=True)),
    url(r'^test/$', RedirectView.as_view(url=reverse_lazy('find_location'),
                                         permanent=True)),
    url(r'^(?P<slug>[-\w]+)/$', RedirectView.as_view(url=reverse_lazy('hub_detail'),
                                                     permanent=True)),
    url(r'^(?P<slug>[-\w]+)/locations.json$', RedirectView.as_view(url=reverse_lazy('hub_locations_json'),
                                                                   permanent=True)),
    url(r'^(?P<slug>[-\w]+)/membership/$', RedirectView.as_view(url=reverse_lazy('hub_membership'),
                                                                permanent=True)),
    url(r'^(?P<slug>[-\w]+)/membership/remove/$', RedirectView.as_view(url=reverse_lazy('hub_membership_remove'),
                                                                       permanent=True)),
    url(r'^(?P<slug>[-\w]+)/edit/$', RedirectView.as_view(url=reverse_lazy('hub_edit'),
                                                          permanent=True)),
]
