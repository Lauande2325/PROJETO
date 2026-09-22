from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'solicitante', 'motorista', 'veiculo',
            'setor', 'atividade', 'origem', 'destino',
            'data', 'horario_saida', 'horario_retorno',
            'quantidade_passageiros', 'status', 'observacoes',
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario_saida': forms.TimeInput(attrs={'type': 'time'}),
            'horario_retorno': forms.TimeInput(attrs={'type': 'time'}),
        }