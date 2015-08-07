from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'MyKitchenHelper.views.home', name='home'),
    url(r'^inventory/', include('items.urls', namespace="inventory")),
    url(r'^recipes/', include('recipes.urls', namespace="recipes")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
]
