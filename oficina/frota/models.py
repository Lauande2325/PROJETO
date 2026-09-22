from django.db import models

class Veiculo(models.Model):
    TIPO_CHOICES = [
        ('leve', 'Leve (Até 4 passageiros)'),
        ('coletivo', 'Coletivo (Até 18 passageiros)'),
    ]
    placa = models.CharField('Placa', max_length=10, unique=True)
    modelo = models.CharField('Modelo', max_length=100)
    tipo = models.CharField('Tipo', max_length=20, choices=TIPO_CHOICES)
    capacidade_maxima = models.IntegerField('Capacidade máxima')
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['placa']
        verbose_name = 'Veículo da frota'

    def __str__(self):
        return f'{self.modelo} [{self.placa}]'