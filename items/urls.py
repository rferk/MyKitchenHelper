from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^regroup$', views.regroup, name='regroup'),
    url(r'^new/$', views.new, name='new'),
    url(r'^edit/$', views.edit, name='edit')
]
