import re

from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome_completo', 'tipo_pessoa', 'cpf_cnpj',
            'telefone', 'whatsapp', 'email',
            'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado',
            'observacoes', 'ativo',
        ]

    def clean_nome_completo(self):
        nome = self.cleaned_data.get('nome_completo', '').strip()
        if not nome:
            raise forms.ValidationError('O nome é obrigatório.')
        return nome

    def clean_cpf_cnpj(self):
        valor = self.cleaned_data.get('cpf_cnpj', '')
        if not valor:
            return valor
        digitos = re.sub(r'\D', '', valor)
        if len(digitos) not in (11, 14):
            raise forms.ValidationError('Informe um CPF ou CNPJ válido.')
        qs = Cliente.objects.filter(cpf_cnpj=valor)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Já existe um cliente com este CPF/CNPJ.')
        return valor