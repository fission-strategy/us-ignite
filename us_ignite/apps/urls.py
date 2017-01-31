from django.conf.urls import  url
from . import views


urlpatterns = [
    url(r'^$', views.app_list, name='app_list'),

    url(r'^sector/(?P<sector>[-\w]+)/$', views.app_list, name='app_list_sector'),
    url(r'^domain/(?P<domain>[-\w]+)/$', views.app_list, name='app_list_sector'),

    # url(r'^category')
    # url(r'^featured/$', views.apps_featured, name='apps_featured'),
    url(r'^(?P<slug>[-\w]+)/$', views.app_detail, name='app_detail'),
    url(r'^stage/(?P<stage>[\d]{1})/$', views.app_list, name='app_list_stage'),

    url(r'^(?P<slug>[-\w]+)/$', views.app_detail, name='app_detail'),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.app_edit, name='app_edit'),
    # url(r'^(?P<slug>[-\w]+)/export/$', views.app_export, name='app_export'),
    # url(r'^add/$', views.app_add, name='app_add'),
]
