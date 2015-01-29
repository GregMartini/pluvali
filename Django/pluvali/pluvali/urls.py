import CopingGame
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^CopingGame/', include('CopingGame.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/login/'}),
	url(r'^register/$', CopingGame.views.register, name='register'),	
	url(r'^$', RedirectView.as_view(url='CopingGame/', permanent=False), name='index'),
]

if settings.DEBUG:
	urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))