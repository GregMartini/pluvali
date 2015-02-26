from django.conf.urls import url, patterns
from django.core.urlresolvers import reverse
from CopingGame import views

urlpatterns = [
	url(r'^$', views.index, name='index'), #homepage
	url(r'^help/', views.help, name='help'), #help page
	url(r'^scenarios/', views.scenario_index, name='scenarios'), #scenario index
	url(r'^(?P<sceneID>\d+)/$', views.game, name='game'), #play game page
	url(r'^victory/', views.victory, name='victory'),
	url(r'^store/', views.store, name='store'),
	url(r'^admin_page/', views.admin_page, name='admin_page/'),
	url(r'^profile/', views.profile, name='profile'),
	
	#mock homepages
	url(r'^h1', views.index1, name='index1'), #homepage
	url(r'^h2', views.index2, name='index2'), #homepage
	url(r'^h3', views.index3, name='index3'), #homepage
]