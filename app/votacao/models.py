# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid


from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime, timedelta
from django.db import models

now = datetime.now()
other_time = now + timedelta(hours=1)


# CreateUpdateModel
# - - - - - - - - - - - - - - - - - - -
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True


# UUIDUser
# - - - - - - - - - - - - - - - - - - -
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class Proposta(models.Model):
    id_user = models.ForeignKey(UUIDUser,on_delete=models.CASCADE,verbose_name='Usuário')
    nome = models.CharField(max_length=255, verbose_name='Lei')
    proposta = models.TextField(verbose_name='proposta')
    tempo_final = models.DateTimeField(verbose_name='Tempo da proposta', default=other_time)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'proposta'
        verbose_name_plural = 'propostas'

class Votacao(models.Model):

    STATUS = (
    (0, 'Negar'),
    (1, 'Aceitar')
            )
    usuario = models.ForeignKey(UUIDUser,on_delete=models.CASCADE,verbose_name='Usuário')
    proposal = models.ForeignKey(Proposta, on_delete=models.CASCADE, verbose_name='Nome da proposta')
    status = models.IntegerField(choices=STATUS)

    class Meta:
        verbose_name = 'Votação'
        verbose_name_plural = 'Votações'

class Comentario(models.Model):

    comentario = models.CharField(max_length=255, null=False, blank=False, verbose_name='Comentário')
    proposta = models.ForeignKey(Proposta,on_delete=models.CASCADE,verbose_name='Proposta')

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'

    

