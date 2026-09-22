from django.contrib import admin

from .models import Servico


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'duracao_estimada_minutos', 'preco', 'ativo')
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria', 'ativo')
    ordering = ('nome',)