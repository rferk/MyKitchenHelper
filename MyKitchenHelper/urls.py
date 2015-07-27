from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'MyKitchenHelper.views.home', name='home'),
    url(r'^inventory/', include('items.urls', namespace="inventory")),
    url(r'^admin/', include(admin.site.urls)),
]
