# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url

from . import views as core




app_name = 'votacao'

urlpatterns = [

    #Home
     path('home/', core.Home.as_view(template_name='core/base.html'), name='home'),

    #Cadastro
     path('usuarios/novo/', core.UserCreateView.as_view(template_name='core/form.html'), name='user-create'),

    #Formulario da Proposta
     path('formprop/', core.Proposta.as_view(), name='formprop'),

    #Formulario de votacao
     path('votacao/', core.Votacao.as_view(), name='votacao'),

    #Aceitar proposta
     path('votar/', core.VotarCreateView.as_view(), name='votar'),
]

