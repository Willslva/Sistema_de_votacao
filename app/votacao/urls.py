# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as core




app_name = 'votacao'

urlpatterns = [
    # Login
     path('login/', auth_views.LoginView.as_view(template_name='core/auth.html'), name='login'),

    # Logout
   
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Index
     path('', core.Index.as_view(template_name='core/base.html'), name='index'),

    #home
     path('home/', core.Home.as_view(template_name='core/home.html'), name='home'),

    #Cadastro
     path('usuarios/novo/', core.UserCreateView.as_view(template_name='core/form.html'), name='user-create'),

    #Formulario da Proposta
     path('formprop/', core.Proposta.as_view(), name='formprop'),

    #Formulario de votacao
     path('votacao/', core.Votacao.as_view(), name='votacao'),

    #Aceitar proposta
     path('votar/', core.VotarCreateView.as_view(), name='votar'),

    #Lista de comentario
     path('addcomentario/', core.Comentarios.as_view(), name='comentarios'),

    #Comentar proposta
     path('comentar/', core.ComentarioCreateView.as_view(), name='comentar'),

    #Lista de comentarios
     path('listcomentarios/', core.ListComentarios.as_view(), name='listcomentarios'),
   

]

