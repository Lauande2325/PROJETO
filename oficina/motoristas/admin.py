from django.contrib import admin
from .models import Motorista


@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnh', 'cpf', 'ativo')
    search_fields = ('nome', 'cnh', 'cpf')
    list_filter = ('ativo',)
    ordering = ('nome',)