from django import forms
from .models import Motorista


class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['usuario', 'nome', 'cnh', 'cpf', 'ativo']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if not nome:
            raise forms.ValidationError('O nome é obrigatório.')
        return nome