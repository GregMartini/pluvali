from django.conf.urls import url, patterns
from CopingGame import views

urlpatterns = [
	url(r'^$', views.index, name='index'),#name='/accounts/index'),
	url(r'^scenarios/', views.scenario_index, name='scenarios'),
	url(r'^(?P<sceneID>\d+)/$', views.game, name='game'),
]