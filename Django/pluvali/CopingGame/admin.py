from django.contrib import admin
from CopingGame.models import *
class SolutionsInline(admin.TabularInline):
	model = Problems.solutions.through
	extra = 3
class ProblemAdmin(admin.ModelAdmin):
	inlines = [SolutionsInline]
	exclude = ('solutions',)

class ProblemsInline(admin.TabularInline):
	model = Scenario.problems.through
	extra = 3
class Player_listInline(admin.TabularInline):
	model = Scenario.player_list.through
	extra = 3
class Group_listInline(admin.TabularInline):
	model = Scenario.group_list.through
	extra = 3
class ScenarioAdmin(admin.ModelAdmin):
	inlines = [ProblemsInline,Player_listInline,Group_listInline]
	exclude = ('problems','player_list','group_list')
class PlayerAdmin(admin.ModelAdmin):
	exclude = ('stage','temp_tokens','scenario_tokens')

admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerGroup)

admin.site.register(Solutions)
admin.site.register(Problems,ProblemAdmin)
admin.site.register(Scenario, ScenarioAdmin)
admin.site.register(Store)
admin.site.register(Purchases)
