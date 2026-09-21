from django.contrib import admin

from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'tipo_pessoa', 'cpf_cnpj', 'telefone', 'email', 'ativo', 'criado_em')
    search_fields = ('nome_completo', 'cpf_cnpj', 'telefone', 'email')
    list_filter = ('tipo_pessoa', 'ativo', 'estado')
    ordering = ('nome_completo',)