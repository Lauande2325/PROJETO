from django.contrib import admin
from .models import Colaborador


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'departamento', 'ativo')
    search_fields = ('nome', 'email', 'cpf', 'departamento')
    list_filter = ('ativo', 'departamento')
    ordering = ('nome',)