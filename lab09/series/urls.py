from . import views
from django.urls import path,re_path
from django.urls import re_path as url

urlpatterns = [
    url(r'^series/$', views.serie_list),
    url(r'^series/(?P<pk>[0-9]+)/$', views.serie_detail),
]
