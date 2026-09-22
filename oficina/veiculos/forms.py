import re

from django import forms

from .models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = [
            'cliente', 'placa', 'marca', 'modelo',
            'ano_fabricacao', 'ano_modelo', 'cor', 'chassi',
            'combustivel', 'quilometragem',
            'observacoes', 'ativo',
        ]

    def clean_placa(self):
        placa = self.cleaned_data.get('placa', '').strip().upper().replace(' ', '')
        if not placa:
            raise forms.ValidationError('A placa é obrigatória.')
        if not re.match(r'^[A-Z]{3}\d[A-Z0-9]\d{2}$', placa):
            raise forms.ValidationError('Informe uma placa válida (padrão antigo ABC1234 ou Mercosul ABC1D23).')
        qs = Veiculo.objects.filter(placa=placa)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Já existe um veículo cadastrado com esta placa.')
        return placa

    def clean_quilometragem(self):
        valor = self.cleaned_data.get('quilometragem')
        if valor is not None and valor < 0:
            raise forms.ValidationError('A quilometragem não pode ser negativa.')
        return valor