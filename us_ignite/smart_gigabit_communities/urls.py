from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reverse-pitch/$', views.reverse_pitch, name='smart_gigabit_communities_reverse_pitch'),
]
