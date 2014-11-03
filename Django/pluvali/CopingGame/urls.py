from django.conf.urls import url, patterns
from CopingGame import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<sceneID>\d+)/$', views.game, name='game'),
]