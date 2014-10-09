import os
from django.db import models
import global_defs as defs

def get_image_path(intstance, filename):
	return os.path.join('users', str(instance.id),filename)

class User(models.Model):
	userID = models.AutoField(primary_key=True)
	userName = models.CharField(max_length=12)
	password = models.CharField(max_length=15)
	email = models.CharField(max_length=30)
	points = models.IntegerField(default=0)
	privileges = models.BooleanField(default=False)
	#avatarPic = FileField(upload_to=get_image_path, blank=True, null=True)

class Scenario(models.Model):
	sceneID = models.AutoField(primary_key=True)
	#media = FileField(upload_to=get_image_path, blank=True, null=True)
	desctiption = models.CharField(max_length=250)
	problems = models.CharField(max_length=500)
	problems = models.CharField(max_length=300)

class SaveState(models.Model):
	userIDfKey = models.ForeignKey(User)
	sceneIDfKey = models.ForeignKey(Scenario)
	uiColor = models.IntegerField(default=defs.BG_WHITE)
	fontColor = models.IntegerField(default=defs.TEXT_BLACK)
	
