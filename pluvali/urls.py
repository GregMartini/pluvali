from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^CopingGame/', include('CopingGame.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/login/'})
]
