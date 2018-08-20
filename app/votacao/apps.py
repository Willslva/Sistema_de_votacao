from django.apps import AppConfig


class VotacaoConfig(AppConfig):
    name = 'app.votacao'

    def ready(self):
    	from . import signals
