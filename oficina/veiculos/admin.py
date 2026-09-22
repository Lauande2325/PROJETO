from django.contrib import admin

from .models import Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'cliente', 'ano_modelo', 'ativo')
    search_fields = ('placa', 'marca', 'modelo', 'cliente__nome_completo')
    list_filter = ('marca', 'combustivel', 'ativo')
    ordering = ('placa',)