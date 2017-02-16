from django.conf.urls import  url
from . import views
from us_ignite.apps import views as apps_views
from us_ignite.testbeds import views as testbeds_views
from us_ignite.resources import views as resources_views
from us_ignite.news import views as news_views

urlpatterns = [
    url(r'^$', views.home_view, name='smart_communities_home'),

    url(r'^applications/$', apps_views.app_list, {'program': 'smart-gigabit-communities'}, name='sgc_apps'),
    url(r'^applications/add/$', apps_views.app_add, {'program': 'smart-gigabit-communities'}, name='sgc_apps_add'),

    url(r'^testbeds/$', testbeds_views.testbed_list, name='testbed_list'),
    url(r'^testbeds/(?P<slug>[-\w]+)/$', testbeds_views.testbed_detail, name='testbed_detail'),
    url(r'^testbeds/(?P<slug>[-\w]+)/locations.json$', testbeds_views.testbed_locations_json,
        name='testbed_locations_json'),

    url(r'^resources/$', resources_views.resource_list, name='sgc_resource_list'),
    url(r'^resources/add/$', resources_views.resource_add, name='sgc_resource_add'),
    url(r'^resources/?(P<slug>[-\w]+)/$', resources_views.resource_detail, name='sgc_resource_detail'),
    url(r'^resources/?(P<slug>[-\w]+)/edit/$', resources_views.resource_edit, name='sgc_resource_edit'),

    url(r'^news/$', news_views.news_post_list, {'program': 'smart-gigabit-communities'}, name='sgc_news'),
]
