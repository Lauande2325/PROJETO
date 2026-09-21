from django.contrib import admin

from .models import Mecanico


@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'especialidade', 'data_admissao', 'ativo')
    search_fields = ('nome', 'cpf', 'especialidade')
    list_filter = ('ativo', 'especialidade')
    ordering = ('nome',)