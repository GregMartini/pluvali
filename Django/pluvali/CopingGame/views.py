#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from CopingGame.models import User, Scenario

def index(request):
	return HttpResponse("Hello Pluvali!")

def index(request):
	scenario_list = Scenario.objects.order_by('title')
	template = loader.get_template('CopingGame/index.html')
	context = RequestContext(request, {
		'scenario_list':scenario_list,
	})
	return HttpResponse(template.render(context))
	
#def homepage(request):
#	user_list = User.object.order_by('userName')[:5]
#	template = loader.get_template('CopingGame/homepage.html')
#	context = RequestContext(requst, {
#		'user_list': user_list,
#	})
#	return HttpResponse(template.render(context))
