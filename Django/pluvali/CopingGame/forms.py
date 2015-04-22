from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from CopingGame.models import Player

class PlayerProfileForm(forms.ModelForm):
	class Meta:
		model = Player
		fields = ('avatarPic',)
	
class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=False)
	
	class Meta:
		model = Player
		fields = ('username', 'email', 'password1', 'password2')
	
	def save(self,commit=True):
		player=super(MyRegistrationForm, self).save(commit=False)
		player.email=self.cleaned_data['email']
		if commit:
			player.save()
		return player
