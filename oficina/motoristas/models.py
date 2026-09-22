from django.conf import settings
from django.db import models

class Motorista(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    nome = models.CharField('Nome', max_length=150)
    cnh = models.CharField('CNH', max_length=20, unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} (CNH: {self.cnh})'