import os
from django.db import models
from django.contrib.auth.models import User
import global_defs as defs

#NOTE ImageField requires Pillow
# run from pluvali dir to install>> pip install pillow  

def get_image_path(intstance, filename):
	return os.path.join('users', str(instance.id),filename)
	
class Player(models.Model):
	user = models.OneToOneField(User)
	email = models.CharField(max_length=30)
	points = models.IntegerField(default=0)
	#avatarPic = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	fav_bg = models.IntegerField(default=defs.BG_WHITE)
	fav_text = models.IntegerField(default=defs.TEXT_BLACK)
	stage = models.IntegerField(default=0) #used for iterating through scenarios
	def __str__(self):
		return self.user.username
	pass
		
class Solutions(models.Model):
	pictureS = models.ImageField(upload_to='/media/solutions/', blank=True, null=True)
	solution = models.CharField(max_length=300, default="Solution")
	def __str__(self):
		return self.solution
	pass

class Problems(models.Model):
	pictureP = models.ImageField(upload_to='/media/problems/', blank=True, null=True)
	problem = models.CharField(max_length=225, default="The Problem.")
	solutions = models.ManyToManyField(Solutions)
	def __str__(self):
		return self.problem
	pass
	
class Scenario(models.Model):
	sceneID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=15, default="Scenario Title")
	description = models.CharField(max_length=250, default="Scenatio Decription")
	problems = models.ManyToManyField(Problems)
	def __str__(self):
		return self.title

class Store(models.Model):
	itemKey = models.AutoField(primary_key=True)
	category = models.CharField(max_length=20, default="Themes")
	itemName = models.CharField(max_length=15, default="ItemName")
	itemDesc = models.CharField(max_length=50, default="Item Description")
	def __str__(self):
		return self.itemName

class Purchases(models.Model):
	player = models.ForeignKey(Player)
	itemFKey = models.ForeignKey(Store)
	def __str__(self):
		return self.itemFKey.itemName
		
		