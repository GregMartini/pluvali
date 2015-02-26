from django import forms
from django.contrib.auth.models import User
from CopingGame.models import Player

class PlayerProfileForm(forms.ModelForm):
		class Meta:
			model = Player
			fields = ('avatarPic',)
