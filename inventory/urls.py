from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add')
]
