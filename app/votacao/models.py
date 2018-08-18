# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid


from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


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

    # core
    name = models.CharField('nome',max_length=100)
    password = models.CharField('senha',max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.IntegerField(verbose_name="CPF")


    
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class Proposta(models.Model):
    proposta = models.TextField(verbose_name='proposta')
    created_time = models.DateTimeField('criado em', auto_now_add=True)


class Votacao(models.Model):

    STATUS = (
    (0, 'Negar'),
    (1, 'Aceitar')
            )
    proposal = models.ForeignKey(Proposta, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True, verbose_name='comment')
    status = models.IntegerField(choices=STATUS)

    

