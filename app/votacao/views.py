# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from . import models
now = datetime.now()

class Index(TemplateView):
    template_name = 'base.html'

class Home(TemplateView):
    template_name = 'home.html'

class UserCreateView(CreateView):
	model = models.UUIDUser
	template_name = 'form.html'
	success_url = reverse_lazy('votacao:home')
	fields = ['username','first_name', 'last_name', 'password', 'email']
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super(UserCreateView, self).form_valid(form)

class Proposta(CreateView):
    model = models.Proposta
    template_name = 'core/formproposta.html'
    success_url = reverse_lazy('votacao:home')
    fields = ['nome','proposta']

    def form_valid(self, form):
         obj = form.save(commit=False)
         obj.id_user = self.request.user
         obj.save()
         return super(Proposta, self).form_valid(form)

class Votacao(ListView):
    model = models.Votacao
    template_name = 'core/votacao.html'
        
    def get_context_data(self, **kwargs):
        kwargs['propostas'] = models.Proposta.objects.all()
        return super(Votacao, self).get_context_data(**kwargs)
           

    
class VotarCreateView(CreateView):
    model = models.Votacao
    template_name = 'core/aceitar.html'
    success_url = reverse_lazy('votacao:home')
    fields = ['proposal', 'status']

    def get_context_data(self, **kwargs):
        kwargs['votacoes'] = models.Votacao.objects.all()
        return super(VotarCreateView, self).get_context_data(**kwargs)

    def get_queryset(self):
         if(now.hour > self.proposal.tempo_final.hour and now.minute > self.proposal.tempo_final.minute):
            Votacao.objects.filter(proposal.tempo_final.hour<now.hour)
            
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return super(VotarCreateView, self).form_valid(form)

class Comentarios(ListView):
    model = models.Comentario
    template_name = 'core/listcomentario.html'

    def get_context_data(self, **kwargs):
        kwargs['propostas'] = models.Proposta.objects.all()
        return super(Comentarios, self).get_context_data(**kwargs)

class ComentarioCreateView(CreateView):
    model = models.Comentario
    template_name = 'core/comentar.html'
    success_url = reverse_lazy('votacao:home')
    fields = ['comentario', 'proposta']

  
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(ComentarioCreateView, self).form_valid(form)

class ListComentarios(ListView):
    model = models.Comentario
    template_name = 'core/comentarios.html'

    def get_context_data(self, **kwargs):
        kwargs['comentarios'] = models.Comentario.objects.all()
        return super(ListComentarios, self).get_context_data(**kwargs)

    





