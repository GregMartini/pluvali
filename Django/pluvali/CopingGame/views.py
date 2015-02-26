from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.core.context_processors import csrf
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from CopingGame.forms import PlayerProfileForm
import random

from CopingGame.models import Player, Scenario, Problems, Solutions, Store, Purchases
from django.contrib.auth.models import User

#login page uses default Django sessions

#link for homepage, requires login
@login_required(login_url='/login')
def index(request):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	context = {'player':player}
	return render(request, 'CopingGame/index.html', context)
	
#MOCK HOMEPAGES
@login_required(login_url='/login')
def index1(request):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	context = {'player':player}
	return render(request, 'CopingGame/index1.html', context)

@login_required(login_url='/login')
def index2(request):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	context = {'player':player}
	return render(request, 'CopingGame/index2.html', context)

@login_required(login_url='/login')
def index3(request):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	context = {'player':player}
	return render(request, 'CopingGame/index3.html', context)


#END MOCH HOMEPAGES

#link for help page
def help(request):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	context = {'player':player}
	return render(request, 'CopingGame/help_page.html', context)

#link for scenario index
@login_required(login_url='/login')
def scenario_index(request):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	scenario_list = Scenario.objects.order_by('title').distinct()
	player.stage = 0
	player.save()
	context = {'scenario_list': scenario_list, 'player':player}
	return render(request, 'CopingGame/scenario_index.html', context)
	
#link for admin page
@login_required(login_url='/login')
def admin_page(request):
	player_list = Player.objects.order_by('user').distinct()
	context = {'player_list':player_list}
	return render(request, 'CopingGame/admin_page.html', context)

#link for game page
@login_required(login_url='/login')
def game(request, sceneID):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	scene = get_object_or_404(Scenario, pk = sceneID)
	max_stage = scene.problems.count()
	stage0 = scene.problems.all()[0]
	if(max_stage >= 2):
		stage1 = scene.problems.all()[1]
	if(max_stage >= 3):
		stage2 = scene.problems.all()[2]
	if(max_stage >= 4):
		stage3 = scene.problems.all()[3]
	if(max_stage >= 5):
		stage4 = scene.problems.all()[4]
	if(player.stage > max_stage):
		player.stage = 0
	if(max_stage >= 1):
		context = {'scene':scene, 'player':player, 'stage0':stage0}
	if(max_stage >= 2):
		context = {'scene':scene, 'player':player, 'stage0':stage0,'stage1':stage1}
	if(max_stage >= 3):
		context = {'scene':scene, 'player':player, 'stage0':stage0,'stage1':stage1,'stage2':stage2}
	if(max_stage >= 4):
		context = {'scene':scene, 'player':player, 'stage0':stage0,'stage1':stage1,'stage2':stage2,'stage3':stage3}
	if(max_stage >= 5):
		context = {'scene':scene, 'player':player, 'stage0':stage0,'stage1':stage1,'stage2':stage2,'stage3':stage3,'stage4':stage4}
	if request.method == 'POST':
		player.tokens += random.randint(2,5)
		player.stage += 1
		player.save()
		if(player.stage == max_stage):
			return render(request, 'CopingGame/victory_page.html', {'player':player})
	
	return render(request, 'CopingGame/game_page.html', context)

@login_required(login_url='/login')
def victory(request):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	player.stage = 0
	player.save()
	context = {'player':player}
	return render(request, 'CopingGame/victory_page.html', context)

@login_required(login_url='/login')
def store(request):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	items_list = Store.objects.order_by('itemName')
	context = {'items_list':items_list, 'player':player}
	if request.method == 'POST':
		#if player.tokens >= 50:  uncomment next two lines for final version
			#player.tokens -= 50
			if 'bluewhite' in request.POST:  #for testing that themes can at least be switched and saved
				player.fav_bg = 'blue'		 #will be implemented in user defaults page next semester
				player.fav_text = 'white'
			if 'firebrickcornsilk' in request.POST:
				player.fav_bg = 'firebrick'
				player.fav_text = 'cornsilk'
			if 'yellowpurple' in request.POST:
				player.fav_bg = 'yellow'
				player.fav_text = 'purple'
			if 'blackorange' in request.POST:
				player.fav_bg = 'black'
				player.fav_text = 'orange'
			if 'defaultblack' in request.POST:
				player.fav_bg = '#ededed'
				player.fav_text = 'black'
			player.save()
	return render(request, 'CopingGame/store_page.html', context)

#User registration
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		player_email = request.POST['email']
		if form.is_valid():
			new_user = form.save()
			new_player = Player.objects.create(user=User.objects.get(username=request.POST['username']), email=player_email)
			new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			return HttpResponseRedirect("/CopingGame/")
		else:
			return render(request, 'registration/register.html', {'form': form,})
	else:
		form = UserCreationForm()
		return render(request, "registration/register.html", {'form': form,})
		
#User profile
@login_required(login_url='/login')
def profile(request):
	player = Player.objects.get(user=User.objects.get(username=request.user))
	purchase_list = Purchases.objects.filter(player=player)
	context = {'player':player, 'purchase_list':purchase_list}
	if request.method == 'POST':
		#Attempt to grab raw data from form information
		a = request.POST
		profileForm = PlayerProfileForm(request.POST, request.FILES)#(data=request.POST)
		if 'avatarPic' in request.Files:
			player.avatarPic = request.FILES['avatarPic']
			player.save()
			context = {'player':player, 'purchase_list':purchase_list, 'profileForm':profileForm}
		return HttpResponseRedirect("CopingGame/profile.html/", context)
	else:
		profileForm = PlayerProfileForm()
		context = {'player':player, 'purchase_list':purchase_list, 'profileForm':profileForm}
		return render(request, "CopingGame/profile.html", context)

