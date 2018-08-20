from django.db.models.signals import pre_save, post_save
from datetime import datetime

from . import models

# Reservation - Pre-save
def votacao_pre_save(sender, instance, **kwargs):
	now = datetime.now()
	if  (now.hour > instance.proposal.tempo_final.hour and now.minute > instance.proposal.tempo_final.minute):
		raise Exception('Desculpe! O prazo de votação foi encerrado.')
  
pre_save.connect(votacao_pre_save, sender=models.Votacao)


