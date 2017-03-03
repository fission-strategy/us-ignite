from django.conf.urls import url
import views


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.program_home, name='program_home'),
]