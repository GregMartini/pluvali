from django import forms
from django.core import validators
from CopingGame.models import Problems

class UploadProblemPicForm(forms.ModelForm):
	class Meta:
		model = Problems
		fields = ('pictureP',)
	