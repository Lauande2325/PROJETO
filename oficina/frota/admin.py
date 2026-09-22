from django.contrib import admin
from .models import Veiculo


@admin.register(Veiculo)
class VeiculoFrotaAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'tipo', 'capacidade_maxima', 'ativo')
    search_fields = ('placa', 'modelo')
    list_filter = ('tipo', 'ativo')
    ordering = ('placa',)