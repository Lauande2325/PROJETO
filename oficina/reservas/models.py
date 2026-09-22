from django.core.exceptions import ValidationError
from django.db import models

from colaboradores.models import Colaborador
from motoristas.models import Motorista
from frota.models import Veiculo

class Reserva(models.Model):
    STATUS_CHOICES = [
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    solicitante = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True, blank=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)

    setor = models.CharField('Setor', max_length=100)
    atividade = models.CharField('Atividade', max_length=150)
    origem = models.CharField('Origem', max_length=150)
    destino = models.CharField('Destino', max_length=150)

    data = models.DateField('Data')
    horario_saida = models.TimeField('Horário de saída')
    horario_retorno = models.TimeField('Horário de retorno')

    quantidade_passageiros = models.IntegerField('Quantidade de passageiros')
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='confirmada')
    observacoes = models.TextField('Observações', blank=True, null=True)
    protocolo_unico = models.CharField('Protocolo', max_length=50, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['-data', '-horario_saida']

    def __str__(self):
        return f'Reserva {self.protocolo_unico or self.pk} - {self.atividade}'

    def clean(self):
        super().clean()

        if self.horario_saida and self.horario_retorno:
            if self.horario_retorno <= self.horario_saida:
                raise ValidationError('O horário de retorno deve ser posterior ao horário de saída.')

        if self.veiculo and self.quantidade_passageiros:
            if self.quantidade_passageiros > 18:
                raise ValidationError('Solicitações acima de 18 passageiros devem ser rejeitadas.')
            if self.veiculo.tipo == 'leve' and self.quantidade_passageiros > 4:
                raise ValidationError('Veículos leves suportam no máximo 4 passageiros.')

        if self.veiculo and self.data and self.horario_saida and self.horario_retorno:
            conflitos = Reserva.objects.filter(
                veiculo=self.veiculo,
                data=self.data,
                status='confirmada',
                horario_saida__lt=self.horario_retorno,
                horario_retorno__gt=self.horario_saida,
            )
            if self.pk:
                conflitos = conflitos.exclude(pk=self.pk)
            if conflitos.exists():
                raise ValidationError('Conflito! Este veículo já está reservado neste período.')