from django.conf.urls import url
from . import views
from us_ignite.apps import views as apps_views
from us_ignite.news import views as news_views


urlpatterns = [
    # url(r'^$', views.home, name='gctc_home'),
    url(r'^action-clusters/$', apps_views.app_list, {'program': 'global-city-team-challenge'}, name='gctc_actionclusters'),
    url(r'^action-clusters/add/$', apps_views.app_add, {'program': 'global-city-team-challenge'}, name='gctc_actionclusters_add'),
    url(r'^action-clusters/archive/(?P<slug>[-\w]+)/$', apps_views.apps_featured_archive, name='gctc_actionclusters_archive'),

    url(r'^news/$', news_views.news_post_list, name='news_post_list'),
]
