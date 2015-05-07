from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from CopingGame.models import Player, Store, Purchase, Scenario

@receiver(post_save, sender=Store)
def model_post_save(sender, instance, created, **kwargs):
	if created:
		players_list = list(Player.objects.all())
		for p in players_list:
			purchase = Purchase.objects.create(player=p, itemFKey=instance, owned=False)
			purchase.save()

@receiver(post_save, sender=Player)
def player_post_save(sender, instance, created, **kwargs):
	if created:
		#add all store items to account
		store_list = list(Store.objects.all())
		for item in store_list:
			#set default purchases to owned
			if item.itemName == 'DefaultBlack':
				purchase = Purchase.objects.create(player=instance, itemFKey=item, owned=True)
				purchase.save()
				instance.fav_bg = item.bg
				instance.fav_text = item.text
				instance.save()
			elif item.itemName == 'DefaultPicture':
				purchase = Purchase.objects.create(player=instance, itemFKey=item, owned=True)
				purchase.save()
				instance.avatarPic = item.itemPicture
				instance.save()
			#set other purchases to not owned	
			else:
				purchase = Purchase.objects.create(player=instance, itemFKey=item, owned=False)
				purchase.save()
		#give access to default scenario
		defaultScenario = Scenario.objects.get(pk=1)
		defaultScenario.player_list.add(instance)
		defaultScenario.save()
			
#@receiver(pre_save, sender=Player)
#def upload_picture_pre_save(sender, instance, created, **kwargs):
#	if created: