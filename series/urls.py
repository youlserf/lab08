from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^series/$', views.serie_list),
    url(r'^series/(?P<pk>[0-9]+)/$', views.serie_detail),
]