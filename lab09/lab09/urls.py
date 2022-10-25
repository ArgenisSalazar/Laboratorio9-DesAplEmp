from django.contrib import admin
from django.urls import path,include,re_path
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('series.urls')),
]
