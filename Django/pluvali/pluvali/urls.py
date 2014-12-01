from django.conf.urls import include, url
from django.contrib import admin
import CopingGame

from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^CopingGame/', include('CopingGame.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/login/'}),
	url(r'^register/$', CopingGame.views.register, name='register'),	
	url(r'^$', RedirectView.as_view(url='CopingGame/', permanent=False), name='index'),
]
