from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from CopingGame.models import Player, Store, Purchase

@receiver(post_save, sender=Store)
def model_post_save(sender, instance, created, **kwargs):
	if created:
		players_list = list(Player.objects.all())
		for p in players_list:
			purchase = Purchase.objects.create(player=p, itemFKey=instance, owned=False)
			purchase.save()
			
#@receiver(pre_save, sender=Player)
#def upload_picture_pre_save(sender, instance, created, **kwargs):
#	if created: