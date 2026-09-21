from django.core.validators import MinValueValidator
from django.db import models


class Peca(models.Model):
    UNIDADE_CHOICES = [
        ('UN', 'Unidade'), ('CX', 'Caixa'), ('PC', 'Peça'),
        ('L', 'Litro'), ('KG', 'Quilograma'), ('M', 'Metro'),
    ]

    codigo = models.CharField('Código', max_length=30, unique=True)
    nome = models.CharField('Nome', max_length=150)
    descricao = models.TextField('Descrição', blank=True)
    fabricante = models.CharField('Fabricante', max_length=100, blank=True)
    categoria = models.CharField('Categoria', max_length=100, blank=True)

    unidade = models.CharField('Unidade', max_length=2, choices=UNIDADE_CHOICES, default='UN')
    estoque_atual = models.IntegerField('Estoque atual', default=0, validators=[MinValueValidator(0)])
    estoque_minimo = models.IntegerField('Estoque mínimo', default=0, validators=[MinValueValidator(0)])
    localizacao = models.CharField('Localização', max_length=100, blank=True)

    preco_custo = models.DecimalField('Preço de custo', max_digits=10, decimal_places=2, default=0,
                                       validators=[MinValueValidator(0)])
    preco_venda = models.DecimalField('Preço de venda', max_digits=10, decimal_places=2, default=0,
                                       validators=[MinValueValidator(0)])

    fornecedor = models.CharField('Fornecedor', max_length=150, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.codigo} - {self.nome}'

    @property
    def estoque_baixo(self):
        return self.estoque_atual <= self.estoque_minimo