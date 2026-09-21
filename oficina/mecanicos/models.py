from django.db import models


class Mecanico(models.Model):
    nome = models.CharField('Nome', max_length=150)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)

    telefone = models.CharField('Telefone', max_length=20, blank=True)
    whatsapp = models.CharField('WhatsApp', max_length=20, blank=True)
    email = models.EmailField('E-mail', blank=True)

    especialidade = models.CharField('Especialidade', max_length=100, blank=True)
    registro_profissional = models.CharField('Registro profissional', max_length=50, blank=True)
    data_admissao = models.DateField('Data de admissão', blank=True, null=True)
    salario_base = models.DecimalField('Salário/base de custo', max_digits=10, decimal_places=2,
                                        blank=True, null=True)

    observacoes = models.TextField('Observações', blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome