import os
from django.db import models
import global_defs as defs

def get_image_path(intstance, filename):
	return os.path.join('users', str(instance.id),filename)

class User(models.Model):
	userID = models.AutoField(primary_key=True)
	userName = models.CharField(max_length=12, default="User")
	password = models.CharField(max_length=15)
	email = models.CharField(max_length=30)
	points = models.IntegerField(default=0)
	privileges = models.BooleanField(default=False)
	#avatarPic = FileField(upload_to=get_image_path, blank=True, null=True)
	def __str__(self):
		return self.userName
		
class Solutions(models.Model):
	#media = FileField(upload_to=get_image_path, blank=True, null=True)
	solution = models.CharField(max_length=300, default="Solution")
	def __str__(self):
		return self.solution

class Problems(models.Model):
	#media = FileField(upload_to=get_image_path, blank=True, null=True)
	problem = models.CharField(max_length=225, default="The Problem.")
	solutions = models.ManyToManyField(Solutions, through='Scenario')
	def __str__(self):
		return self.problem
		
class Scenario(models.Model):
	sceneID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=15, default="Scenario Title")
	description = models.CharField(max_length=250, default="Scenatio Decription")
	problems = models.ForeignKey(Problems)
	solutions = models.ForeignKey(Solutions)
	def __str__(self):
		return self.title

class SaveState(models.Model):
	userIDfKey = models.ForeignKey(User)
	sceneIDfKey = models.ForeignKey(Scenario)
	uiColor = models.IntegerField(default=defs.BG_WHITE)
	fontColor = models.IntegerField(default=defs.TEXT_BLACK)

class Store(models.Model):
	itemKey = models.AutoField(primary_key=True)
	itemName = models.CharField(max_length=15, default="ItemName")
	itemDesc = models.CharField(max_length=50, default="Item Description")
	def __str__(self):
		return self.itemName
