from django.conf.urls import url
from CopingGame import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]