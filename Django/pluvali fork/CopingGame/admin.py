from django.contrib import admin
from CopingGame.models import Scenario

class ScenarioAdmin(admin.ModelAdmin):
	fieldsets = [
		('Scenario Title', {'fields': ['title']}),
		('Description',    {'fields': ['description'], 'classes': ['collapse']}),
		('Problems',    {'fields': ['problems'], 'classes': ['collapse']}),
		('Solutions',    {'fields': ['solutions'], 'classes': ['collapse']}),
	]