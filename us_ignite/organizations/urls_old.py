from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('organization_list'), permanent=True)),
    url(r'^(?P<slug>[-\w]+)/$', RedirectView.as_view(url=reverse_lazy('organization_detail'), permanent=True)),
    url(r'^(?P<slug>[-\w]+)/edit/$', RedirectView.as_view(url=reverse_lazy('organization_edit'), permanent=True)),
]