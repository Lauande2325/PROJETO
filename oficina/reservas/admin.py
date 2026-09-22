from django.contrib import admin
from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('atividade', 'veiculo', 'motorista', 'data', 'horario_saida', 'horario_retorno', 'status')
    search_fields = ('atividade', 'setor', 'protocolo_unico')
    list_filter = ('status', 'data')
    ordering = ('-data', '-horario_saida')