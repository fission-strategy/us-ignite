from django.conf.urls import url
from . import views
from us_ignite.apps import views as apps_views

urlpatterns = [
    # url(r'^$', views.home, name='gctc_home'),
    url(r'^applications/$', apps_views.app_list, {'program': 'global-city-team-challenge'}, name='gctc_actionclusters'),
    url(r'^applications/add/$', apps_views.app_add, {'program': 'global-city-team-challenge'}, name='gctc_actionclusters_add'),
    # url(r'^action-clusters/archive/(?P<slug>[-\w]+)/$', views.actionclusters_archive, name='gctc_actionclusters_archive'),
    # url(r'^news/$', ),
]
