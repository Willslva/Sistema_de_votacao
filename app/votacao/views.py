# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models

class Home(TemplateView):
    template_name = 'base.html'

class UserCreateView(CreateView):
	model = models.UUIDUser
	template_name = 'form.html'
	success_url = reverse_lazy('votacao:votacao')
	fields = ['name', 'password', 'email', 'cpf']
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super(UserCreateView, self).form_valid(form)

class Proposta(CreateView):
    model = models.Proposta
    template_name = 'core/formproposta.html'
    success_url = reverse_lazy('votacao:home')
    fields = ['proposta']

    def form_valid(self, form):
         obj = form.save(commit=False)
         obj.user = self.request.user
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
    fields = ['proposal', 'comment', 'status']

  
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(VotarCreateView, self).form_valid(form)



