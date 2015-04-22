from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from CopingGame.models import *
from django import forms

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
	
class PlayerChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = Player
		
class PlayerCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = Player
	
	def clean_username(self):
		username = self.cleaned_daya['username']
		try:
			Player.objects.get(username=username)
		except Player.DoesNotExist:
			return username
		raise forms.ValidationError(self.error_messages['duplicate_username'])

class PlayerAdmin(UserAdmin):
	form = PlayerChangeForm
	add_form = PlayerCreationForm
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('tokens', 'avatarPic', 'fav_bg','fav_text', 'text_size',)}),
	)

admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerGroup)
admin.site.register(Scenario, ScenarioAdmin)
admin.site.register(Problems,ProblemAdmin)
admin.site.register(Solutions)

admin.site.register(Store)
admin.site.register(Purchases)
