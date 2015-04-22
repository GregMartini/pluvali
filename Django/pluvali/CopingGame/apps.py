from django.apps import AppConfig

class MyAppConfig(AppConfig):
	name = 'CopingGame'
	
	def ready(self):
		import CopingGame.signals