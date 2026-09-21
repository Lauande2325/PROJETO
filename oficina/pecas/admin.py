from django.contrib import admin

from .models import Peca


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'fabricante', 'categoria', 'estoque_atual', 'preco_venda', 'ativo')
    search_fields = ('codigo', 'nome', 'fabricante', 'categoria')
    list_filter = ('categoria', 'ativo', 'unidade')
    ordering = ('nome',)