from django import forms
from .models import Colaborador


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'email', 'cpf', 'departamento', 'ativo']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if not nome:
            raise forms.ValidationError('O nome é obrigatório.')
        return nome

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        if not email:
            raise forms.ValidationError('O email é obrigatório.')
        return email

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf', '').strip()
        if not cpf:
            raise forms.ValidationError('O CPF é obrigatório.')
        return cpf

    def clean_departamento(self):
        departamento = self.cleaned_data.get('departamento', '').strip()
        if not departamento:
            raise forms.ValidationError('O departamento é obrigatório.')
        return departamento