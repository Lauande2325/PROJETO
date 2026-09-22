from django import forms

from .models import Servico


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = [
            'nome', 'categoria', 'duracao_estimada_minutos', 'preco',
            'descricao', 'ativo',
        ]

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if not nome:
            raise forms.ValidationError('O nome é obrigatório.')
        return nome

    def clean_duracao_estimada_minutos(self):
        valor = self.cleaned_data.get('duracao_estimada_minutos')
        if valor is not None and valor <= 0:
            raise forms.ValidationError('A duração estimada deve ser maior que zero.')
        return valor

    def clean_preco(self):
        valor = self.cleaned_data.get('preco')
        if valor is not None and valor < 0:
            raise forms.ValidationError('O preço não pode ser negativo.')
        return valor