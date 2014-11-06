from django.conf.urls import url, patterns
from django.contrib.auth.views import login
from CopingGame import views

urlpatterns = [
	url(r'^$', views.index, name='/accounts/index'),
	url(r'^(?P<sceneID>\d+)/$', views.game, name='game'),
	url(r'^login/', 'CopingGame.views.login', name='login'),
]