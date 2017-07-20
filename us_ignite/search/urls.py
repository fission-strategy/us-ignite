from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^apps/$', views.search_apps, name='search_apps'),
    url(r'^communities/$', views.search_hubs, name='search_hubs'),
    # url(r'^events/$', 'search_events', name='search_events'),
    # url(r'^hubs/$', 'search_hubs', name='search_hubs'),
    # url(r'^actionclusters/$', 'search_actionclusters', name='search_actionclusters'),
    # url(r'^orgs/$', 'search_organizations', name='search_organizations'),
    # url(r'^resources/$', 'search_resources', name='search_resources'),
    # url(r'^tags.json$', 'tag_list', name='tag_list'),
]
