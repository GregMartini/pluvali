from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.core.context_processors import csrf
from django.db.models import Q
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from CopingGame.forms import PlayerProfileForm
import random

from CopingGame.models import Player, Scenario, Problems, Solutions, Store, Purchases

#login page uses default Django sessions

#link for homepage, requires login
@login_required(login_url='/login')
def index(request):
	player = Player.objects.get(username=request.user)
	context = {'player':player}
	return render(request, 'CopingGame/index.html', context)

#link for help page
def help(request):
	player = Player.objects.get(username=request.user)
	context = {'player':player}
	return render(request, 'CopingGame/help_page.html', context)

#link for scenario index
@login_required(login_url='/login')
def scenario_index(request):
	player = Player.objects.get(username=request.user)
	#Pull scenario list by associated to the PLAYER by Player_List or Player_Group_List
	scenario_list = Scenario.objects.filter(Q(player_list=player) | Q(group_list__player=player)).distinct()
	#set stage to 0 in case viewing different scenario than previously.
	player.stage = 0
	player.scenario_tokens = 0
	player.tokens_earned = str("0,0,0,0,0")
	player.save()
	context = {'scenario_list': scenario_list, 'player':player}
	return render(request, 'CopingGame/scenario_index.html', context)
	
#link for admin page
@login_required(login_url='/login')
def admin_page(request):
	player_list = Player.objects.order_by('username').distinct()
	context = {'player_list':player_list}
	return render(request, 'CopingGame/admin_page.html', context)
	
#link for game page
@login_required(login_url='/login')
def game(request, sceneID):
	player = Player.objects.get(username=request.user)
	scene = get_object_or_404(Scenario, pk = sceneID)
	#In case Player navigates  by typing scenario in url
	max_stage = scene.problems.count()
	if(player.stage > max_stage):
		player.stage = 0
		player.save()
	#Check if player is on first stage and tokens_earned hasn't been populated
	if(player.stage == 0 and player.tokens_earned == str("0,0,0,0,0")):
		#populate tokens earned for this scenario
		player.tokens_earned = random.randint(2,5),random.randint(2,5),random.randint(2,5),random.randint(2,5),random.randint(2,5)
		player.save()
	#Parse into list
	tokens_list = str(player.tokens_earned).lstrip('(').rstrip(')').split(',')
	#Get max number of stages in scenario
	stage0 = scene.problems.all()[0]
	if(max_stage >= 2):
		stage1 = scene.problems.all()[1]
	if(max_stage >= 3):
		stage2 = scene.problems.all()[2]
	if(max_stage >= 4):
		stage3 = scene.problems.all()[3]
	if(max_stage >= 5):
		stage4 = scene.problems.all()[4]
	#Fill context
	if(max_stage == 1):
		context = {'scene':scene, 'player':player, 'stage0':stage0, 'tokens0':tokens_list[0] }
	if(max_stage == 2):
		context = {'scene':scene, 'player':player, 'stage0':stage0,'stage1':stage1, 'tokens0':tokens_list[0], 'tokens1':tokens_list[1]}
	if(max_stage == 3):
		context = {'scene':scene, 'player':player, 'stage0':stage0,'stage1':stage1,'stage2':stage2, 'tokens0':tokens_list[0], 'tokens1':tokens_list[1], 'tokens2':tokens_list[2]}
	if(max_stage == 4):
		context = {'scene':scene, 'player':player, 'stage0':stage0,'stage1':stage1,'stage2':stage2,'stage3':stage3, 'tokens0':tokens_list[0], 'tokens1':tokens_list[1], 'tokens2':tokens_list[2], 'tokens3':tokens_list[3]}
	if(max_stage == 5):
		context = {'scene':scene, 'player':player, 'stage0':stage0,'stage1':stage1,'stage2':stage2,'stage3':stage3,'stage4':stage4, 'tokens0':tokens_list[0], 'tokens1':tokens_list[1], 'tokens2':tokens_list[2], 'tokens3':tokens_list[3], 'tokens4':tokens_list[4]}
	#When player selects an answer, award tokens and move to next stage
	if request.method == 'POST':
		if(player.stage == 0):
			player.scenario_tokens = int(tokens_list[0])
			player.tokens += int(tokens_list[0])
		if(player.stage == 1):
			player.scenario_tokens += int(tokens_list[1])
			player.tokens += int(tokens_list[1])
		if(player.stage == 2):
			player.scenario_tokens += int(tokens_list[2])
			player.tokens += int(tokens_list[2])
		if(player.stage == 3):
			player.scenario_tokens += int(tokens_list[3])
			player.tokens += int(tokens_list[3])
		if(player.stage == 4):
			player.scenario_tokens += int(tokens_list[4])
			player.tokens += int(tokens_list[4])
		#Move player to next stage in scenario
		player.stage += 1
		player.save()
		if(player.stage == max_stage):
			return HttpResponseRedirect("/CopingGame/victory/")	
	return render(request, 'CopingGame/game_page.html', context)

@login_required(login_url='/login')
def victory(request):
	player = Player.objects.get(username=request.user)
	player.stage = 0
	player.save()
	context = {'player':player}
	return render(request, 'CopingGame/victory_page.html', context)
	
#Store themes section
@login_required(login_url='/login')
def store_themes(request):
	player = Player.objects.get(username=request.user)
	purchase_list = Purchases.objects.filter(player=player)
	theme_list = purchase_list.filter(itemFKey__category='Themes')
	theme_names = theme_list.values('itemFKey__itemName').distinct()
	context = {'player':player, 'purchase_list':purchase_list, 'theme_list':theme_list, 'theme_names':theme_names}
	if request.method == 'POST':
		if 'change' in request.POST:
			theme = Store.objects.get(itemName=request.POST.get("change","")) #Get the specific theme from store items
			player.fav_bg = theme.bg #Set background color to the themes background color
			player.fav_text = theme.text #Set the text color to the themes text color
			player.save() #Save the player settings
		if 'buy' in request.POST:
			player.tokens -= 50 #Deduct the players token total
			theme = purchase_list.get(itemFKey__itemName=request.POST.get("buy","")) #Get the specific theme the user wishes to buy
			theme.owned = True #Say that the player now owns the theme
			theme.save() #Save the theme purchase
			player.fav_bg = theme.itemFKey.bg #Set background color to the themes background color
			player.fav_text = theme.itemFKey.text #Set the text color to the themes text color
			player.save() #Save the player settings
	return render(request, 'CopingGame/store_themes.html', context)

#Store user pictures section
@login_required(login_url='/login')
def store_user_pictures(request):
	player = Player.objects.get(username=request.user)
	purchase_list = Purchases.objects.filter(player=player)
	picture_list = purchase_list.filter(itemFKey__category='Pictures')
	picture_names = picture_list.values('itemFKey__itemName').distinct()
	context = {'player':player, 'purchase_list':purchase_list, 'picture_list':picture_list, 'picture_names':picture_names}
	if request.method == 'POST':
		if 'change' in request.POST:
			picture = Store.objects.get(itemName=request.POST.get("change","")) #Get the specific picture from store items
			player.avatarPic = picture.itemPicture.url #Change the users picture
			player.save() #Save the player settings
		if 'buy' in request.POST:
			player.tokens -= 50 #Deduct the players token total
			picture = purchase_list.get(itemFKey__itemName=request.POST.get("buy","")) #Get the specific picture the user wishes to buy
			picture.owned = True #Say that the player now owns the picture
			picture.save() #Save the theme purchase
			player.avatarPic = picture.itemFKey.itemPicture.url #Change the users picture to the purchased one
			player.save() #Save the player settings
	return render(request, 'CopingGame/store_user_pictures.html', context)

from CopingGame.forms import MyRegistrationForm
#Player registration
def register(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		player_email = request.POST['email']
		if form.is_valid():
			#create new PLAYER from form
			new_player = form.save()
			new_player = authenticate(username=request.POST['username'], password=request.POST['password1'])
			#add all store items to account
			store_list = list(Store.objects.all())
			for item in store_list:
				#set default purchases to owned
				if item.itemName == 'DefaultBlack':
					purchase = Purchases.objects.create(player=new_player, itemFKey=item, owned=True)
					purchase.save()
					new_player.fav_bg = item.bg
					new_player.fav_text = item.text
					new_player.save()
				elif item.itemName == 'DefaultPicture':
					purchase = Purchases.objects.create(player=new_player, itemFKey=item, owned=True)
					purchase.save()
					new_player.avatarPic = item.itemPicture
					new_player.save()
				#set other purchases to not owned	
				else:
					purchase = Purchases.objects.create(player=new_player, itemFKey=item, owned=False)
					purchase.save()
			#give access to default scenario
			defaultScenario = Scenario.objects.get(pk=1)
			defaultScenario.player_list.add(new_player)
			defaultScenario.save()
			return HttpResponseRedirect("/CopingGame/")
		else:
			return render(request, 'registration/register.html', {'form': form,})
	else:
		form = UserCreationForm()
		return render(request, "registration/register.html", {'form': form,})

#Player profile
@login_required(login_url='/login')
def profile(request):
	player = Player.objects.get(username=request.user)
	purchase_list = Purchases.objects.filter(player=player, owned=True)
	context = {'player':player, 'purchase_list':purchase_list}
	if request.method == 'POST':
		if 'smallFont' in request.POST:
			player.text_size = 5
			player.save()
		elif 'mediumFont' in request.POST:
			player.text_size = 6
			player.save()
		elif 'largeFont' in request.POST:
			player.text_size = 7
			player.save()
		elif 'upload' in request.POST:
			profileForm = PlayerProfileForm(request.POST, request.FILES)
			if profileForm.is_valid():
				try:
					picture=request.FILES['avatarPic']
					player.avatarPic=picture
					player.save()
					return redirect('CopingGame/profile.html')
				except Exception as e:
					return redirect('CopingGame/profile.html')
		elif 'theme' in request.POST:
			theme = Store.objects.get(itemName=request.POST.get("theme","")) #Get the specific theme
			player.fav_bg = theme.bg #Set background color to the themes background color
			player.fav_text = theme.text #Set the text color to the themes text color
			player.save()
		elif 'picture' in request.POST:
			player.avatarPic = request.POST.get("picture", "") #Change user picture to the selected one
			player.save()
		return render(request, "CopingGame/profile.html", context)
	else:
		profileForm = PlayerProfileForm()
		context = {'player':player, 'purchase_list':purchase_list, 'profileForm':profileForm}
		return render(request, "CopingGame/profile.html", context)

