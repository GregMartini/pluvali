from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.core.context_processors import csrf

from CopingGame.models import User, Scenario


def login(request):
	logout(request)
	username = password = ''
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('index')
	context = { 'username':username}
	context.update(csrf(request))
	return render(request, 'registration/login.html', context)
	
#link for scenario index
#@login_required
def index(request):
#	if not request.user.is_authenticated():
#		return redirect(request, 'CopingGame/login_page.html')
	scenario_list = Scenario.objects.order_by('title')
	context = {'scenario_list': scenario_list}
	return render(request, 'CopingGame/index.html', context)
	
#link for game page
@login_required	
def game(request, sceneID):
	scene = get_object_or_404(Scenario, pk = sceneID)
	return render(request, 'CopingGame/game_page.html', {'scene': scene})
	

#def homepage(request):
#	user_list = User.object.order_by('userName')[:5]
#	template = loader.get_template('CopingGame/homepage.html')
#	context = RequestContext(requst, {
#		'user_list': user_list,
#	})
#	return HttpResponse(template.render(context))
