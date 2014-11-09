from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.core.context_processors import csrf

from CopingGame.models import User, Scenario

#link for homepage, requires login
@login_required(login_url='/login')
def index(request):
	return render(request, 'CopingGame/index.html')

#link for scenario index
def scenario_index(request):
	scenario_list = Scenario.objects.order_by('title')
	context = {'scenario_list': scenario_list}
	return render(request, 'CopingGame/scenario_index.html', context)
	
#link for game page
#@login_required	
def game(request, sceneID):
	scene = get_object_or_404(Scenario, pk = sceneID)
	return render(request, 'CopingGame/game_page.html', {'scene': scene})
	