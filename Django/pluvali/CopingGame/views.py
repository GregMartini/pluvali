from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.core.context_processors import csrf

from CopingGame.models import User, Scenario, Problems, Solutions, Store

#login page uses default Django sessions

#link for homepage, requires login
@login_required(login_url='/login')
def index(request):
	return render(request, 'CopingGame/index.html')

#link for help page
def help(request):
	return render(request, 'CopingGame/help_page.html')

#link for scenario index
@login_required(login_url='/login')
def scenario_index(request):
	scenario_list = Scenario.objects.order_by('title')
	context = {'scenario_list': scenario_list}
	return render(request, 'CopingGame/scenario_index.html', context)
	
#link for game page
@login_required(login_url='/login')
def game(request, sceneID):
	scene = get_object_or_404(Scenario, pk = sceneID)
	problems = scene.problems
	#solutions = problems.solutions
	context = {'scene':scene, 'problems':problems}
	return render(request, 'CopingGame/game_page.html', context)

@login_required(login_url='/login')
def store(request):
	items_list = Store.objects.order_by('itemName')
	context = {'items_list':items_list}
	return render(request, 'CopingGame/store_page.html', context)

#User registration
