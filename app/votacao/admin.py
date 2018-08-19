# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import UUIDUser, Proposta, Votacao, Comentario


# UserAdmin
# - - - - - - - - - - - - - - - - - - -
class UserAdmin(auth.UserAdmin):

    fieldsets = (
        ('Personal info', {'fields': ('name', 'password',  'email', 'cpf')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions')


# Register
# - - - - - - - - - - - - - - - - - - -
admin.site.register(UUIDUser, UserAdmin)
admin.site.register(Proposta)
admin.site.register(Votacao)
admin.site.register(Comentario)