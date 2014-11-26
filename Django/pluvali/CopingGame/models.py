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
	fav_bg = models.CharField(max_length=30, default='#ededed')
	fav_text = models.CharField(max_length=30, default='black')
	stage = models.IntegerField(default=0) #used for iterating through scenarios
	def passw (self):
		return self.user.password
	def __str__(self):
		return self.user.username
	pass
		
class Solutions(models.Model):
	pictureS = models.ImageField(upload_to='/media/solutions/', blank=True, null=True)
	solution = models.CharField(max_length=300, default="Solution")
	def __str__(self):
		return self.solution
	pass

def upload_path_handler(instance, filename):
	return filename
	
class Problems(models.Model):
	pictureP = models.ImageField(upload_to=upload_path_handler, blank=True, null=True)
	problem = models.CharField(max_length=225, default="The Problem.")
	solutions = models.ManyToManyField(Solutions)
	def __str__(self):
		return self.problem
		
	def __str__(self):
		return self.problem
	def save(self, *args, **kwargs):
		self_pk = self.pk
		problem_id = self.problem_id
		problem_id_str = str(problem_id)
		
		new_file = generate_image_name_hash()
		new_file_main = new_file + '.jpg'
		new_file_root_path = settings.PROBLEMS_UPLOAD_PATH + '/' + problem_id_str + '/' +new_file_main
		
		if self.pictureP:
			self.pictureP.name = settings.PROBLEMS_UPLOAD_PATH + '/' + problem_id_str + '/' +new_file_main
			
		if self.pictureP and not self_pk:
			super(Problems, self).save(*args, **kwargs)
		
		if self.pictureP and self_pk:
			old_img = Picture.objects.get(pk=self.pk)
			old_img_instance = old_img.pictureP
			
		if self.pictureP:
			if self_pk:
				pictureP = old_img_instance
			else:
				pictureP = self.pictureP
		
		super(Problems, self).save(*args, **kwargs)
		
		#if in form
		if self.pictureP:
			tmp_file = Image.open(self.pictureP.path)
			if tmp_file.mode != 'RGB':
				tmp_file = tmp_file.convert('RGB')
			
			image = Image.open(self.pictureP.path)
			if pictureP.mode != 'RGB':
				pictureP = pictureP.convert('RGB')
			pictureP.save(new_file_root_path, 'JPEG', quality=100)
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
		
		
