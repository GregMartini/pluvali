from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.core.context_processors import csrf
from django import forms
from django.contrib.auth.forms import UserCreationForm #wont need here if registrationForm is overridden
from CopingGame.forms import RegistrationForm #might not need if cant override UserCreationForm

from CopingGame.models import Player, Scenario, Problems, Solutions, Store
from django.contrib.auth.models import User

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
	solutions = scene.solutions
	context = {'scene':scene, 'problems':problems, 'solutions':solutions}
	if request.method == 'POST':
		p = Player.objects.get(user=request.user)
		p.points += 1
		
	return render(request, 'CopingGame/game_page.html', context)

@login_required(login_url='/login')
def store(request):
	items_list = Store.objects.order_by('itemName')
	context = {'items_list':items_list}
	return render(request, 'CopingGame/store_page.html', context)

#User registration
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			
			new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			return HttpResponseRedirect("/CopingGame/")
		else:
			return render(request, 'registration/register.html', {'form': form,})
	else:
		form = UserCreationForm()
		return render(request, "registration/register.html", {'form': form,})
	