from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.mailing_subscribe, name='mailing_subscribe'),
    url(r'^(?P<slug>[-\w]+)/$', views.mailing_subscribe, name='mailing_subscribe'),
]
