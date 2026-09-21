from django import forms

from .models import Peca


class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = [
            'codigo', 'nome', 'fabricante', 'categoria',
            'unidade', 'estoque_atual', 'estoque_minimo', 'localizacao',
            'preco_custo', 'preco_venda', 'fornecedor', 'descricao', 'ativo',
        ]

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo', '').strip()
        if not codigo:
            raise forms.ValidationError('O código é obrigatório.')
        qs = Peca.objects.filter(codigo__iexact=codigo)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Já existe uma peça cadastrada com este código.')
        return codigo

    def clean_estoque_atual(self):
        valor = self.cleaned_data.get('estoque_atual')
        if valor is not None and valor < 0:
            raise forms.ValidationError('O estoque atual não pode ser negativo.')
        return valor

    def clean_estoque_minimo(self):
        valor = self.cleaned_data.get('estoque_minimo')
        if valor is not None and valor < 0:
            raise forms.ValidationError('O estoque mínimo não pode ser negativo.')
        return valor

    def clean_preco_custo(self):
        valor = self.cleaned_data.get('preco_custo')
        if valor is not None and valor < 0:
            raise forms.ValidationError('O preço de custo não pode ser negativo.')
        return valor

    def clean_preco_venda(self):
        valor = self.cleaned_data.get('preco_venda')
        if valor is not None and valor < 0:
            raise forms.ValidationError('O preço de venda não pode ser negativo.')
        return valor