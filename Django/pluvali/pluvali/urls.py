from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^CopingGame/', include('CopingGame.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
