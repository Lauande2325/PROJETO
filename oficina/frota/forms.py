from django import forms
from .models import Veiculo


class VeiculoFrotaForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'modelo', 'tipo', 'capacidade_maxima', 'ativo']

    def clean_capacidade_maxima(self):
        valor = self.cleaned_data.get('capacidade_maxima')
        if valor is not None and valor <= 0:
            raise forms.ValidationError('A capacidade máxima deve ser maior que zero.')
        return valor