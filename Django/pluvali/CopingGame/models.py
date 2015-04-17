import os
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

#NOTE ImageField requires Pillow
# run from pluvali dir to install>> pip install pillow  

	
class Player(models.Model):
	user = models.OneToOneField(User)
	email = models.CharField(max_length=30)
	tokens = models.IntegerField(default=0)
	avatarPic = models.ImageField(upload_to='userPic/', default='userPic/default-user.png')
	fav_bg = models.CharField(max_length=30, default='#ededed')
	fav_text = models.CharField(max_length=30, default='black')
	text_size = models.IntegerField(default=6)
	stage = models.IntegerField(default=0) #used for iterating through scenarios
	scenario_tokens = models.IntegerField(default=0) #used for tracking player's tokens in a scenario
	tokens_earned = models.CharField(max_length=9, default="0,0,0,0,0") #Used to randomly generate tokens earned in a scenario
	def passw (self):
		return self.user.password
	def __str__(self):
		return self.user.username
	pass

class PlayerGroup(models.Model):
	groupName = models.CharField(max_length=35, default="Admin's Group")
	player = models.ManyToManyField(Player)
	def __str__(self):
		return self.groupName
	pass
	
class Solutions(models.Model):
	pictureS = models.ImageField(upload_to='solutions/', blank=True, null=True)
	solution = models.CharField(max_length=300, default="Solution")
	sVideoId = models.CharField(max_length=50, default="q_g7s2oBzCw") #Clorox commercial, change this
	verbose_name_plural = 'Solutions'
	def __str__(self):
		return self.solution
	
	pass
	
class Problems(models.Model):
	pictureP = models.ImageField(upload_to='problems/', null=True)
	problem = models.CharField(max_length=225, default="The Problem.")
	solutions = models.ManyToManyField(Solutions)
	pVideoId = models.CharField(max_length=50, default="q_g7s2oBzCw") #Clorox commercial, change this
	def __str__(self):
		return self.problem
	verbose_name_plural = 'Problems'
	pass
	
class Scenario(models.Model):
	sceneID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=35, default="Scenario Title")
	description = models.CharField(max_length=250, default="Scenatio Decription")
	problems = models.ManyToManyField(Problems)
	player_list = models.ManyToManyField(Player, blank=True)
	group_list = models.ManyToManyField(PlayerGroup, blank=True)
	def __str__(self):
		return self.title

class Store(models.Model):
	itemKey = models.AutoField(primary_key=True)
	category = models.CharField(max_length=20, default="Themes")
	itemName = models.CharField(max_length=15, default="ItemName")
	itemDesc = models.CharField(max_length=50, default="Item Description")
	itemPicture = models.ImageField(upload_to='store/', blank=True, null=True)
	value1 = models.CharField(max_length=10, blank=True)
	value2 = models.CharField(max_length=10, blank=True)
	def __str__(self):
		return self.itemName
	verbose_name_plural = 'StoreItems'

class Purchases(models.Model):
	player = models.ForeignKey(Player)
	itemFKey = models.ForeignKey(Store)
	owned = models.BooleanField(default=False)
	def __str__(self):
		name = self.player.user.username+'-'+self.itemFKey.itemName
		return name
	verbose_name_plural = 'Purchases'
		
def upload_path_handler(self):
	return
