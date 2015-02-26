from django import forms
from django.contrib.auth.models import User
#from django.core import validators
from CopingGame.models import Player

class PlayerProfileForm(forms.ModelForm):
		class Meta:
			model = Player
			fields = ('avatarPic',)
