from django import forms

from .models import Mecanico


class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = [
            'nome', 'cpf',
            'telefone', 'whatsapp', 'email',
            'especialidade', 'registro_profissional', 'data_admissao',
            'observacoes', 'ativo',
        ]

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if not nome:
            raise forms.ValidationError('O nome é obrigatório.')
        return nome