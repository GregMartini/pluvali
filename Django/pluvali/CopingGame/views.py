#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
#from django.http import Http404

from CopingGame.models import User, Scenario

#link for scenario index
def index(request):
    scenario_list = Scenario.objects.order_by('title')
    context = {'scenario_list': scenario_list}
    return render(request, 'CopingGame/index.html', context)
	
#link for game page	
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
