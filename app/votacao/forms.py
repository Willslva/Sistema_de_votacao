#coding:utf-8
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UUIDUser, Proposta, Votacao

# User: create
class UUIDUserForm(forms.ModelForm):

    def save(self, commit=True):
        user = super(UUIDUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = UUIDUser
        fields = ('username', 'first_name', 'email', 'password')
        labels = {
            'username': 'Login',
            'first_name': 'Nome completo',
            'email': 'Email',
        }
        widgets={
            'password': forms.PasswordInput()
}


#Proposta
class PropostaForm(forms.ModelForm):
    nome = forms.TextField(widgets=forms.TextField())
    proposta = forms.TextField(widgets=forms.TextField())
    created_time = forms.DateTimeField(widgets=forms.HiddenField(),initial=datetime.now())

    def save(self, commit=True):
        prop = super(PropostaForm, self).save(commit=False)
        if commit:
            prop.save()
        return prop
    class Meta:
        model = Proposta
        fields = ('nome','proposta','created_time')

#Votacao
class VotacaoForm(forms.ModelForm):
    usuario = forms.TextField(widgets=forms.TextField())
    proposal = forms.ForeignKey(widgets=forms.HiddenField())
    status = forms.IntegerField(widgets=forms.IntegerField(), initial=1)
    def save(self, commit=True):
        votar = super(VotacaoForm, self).save(commit=False)
        if commit:
            votar.save()
        return votar
    class Meta:
        model = Votacao

        fields = ('proposal', 'status')