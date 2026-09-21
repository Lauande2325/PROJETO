from django.db import models


class Cliente(models.Model):
    TIPO_PESSOA_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    nome_completo = models.CharField('Nome completo', max_length=150)
    tipo_pessoa = models.CharField('Tipo de pessoa', max_length=2, choices=TIPO_PESSOA_CHOICES, default='PF')
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, unique=True, blank=True, null=True)

    telefone = models.CharField('Telefone', max_length=20, blank=True)
    whatsapp = models.CharField('WhatsApp', max_length=20, blank=True)
    email = models.EmailField('E-mail', blank=True)

    cep = models.CharField('CEP', max_length=9, blank=True)
    endereco = models.CharField('Endereço', max_length=150, blank=True)
    numero = models.CharField('Número', max_length=10, blank=True)
    complemento = models.CharField('Complemento', max_length=100, blank=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True)
    estado = models.CharField('UF', max_length=2, blank=True)

    observacoes = models.TextField('Observações', blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Data de cadastro', auto_now_add=True)
    atualizado_em = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        ordering = ['nome_completo']

    def __str__(self):
        return self.nome_completo

    def save(self, *args, **kwargs):
        if not self.cpf_cnpj:
            self.cpf_cnpj = None
        super().save(*args, **kwargs)

    @property
    def endereco_completo(self):
        partes = []
        if self.endereco:
            linha = self.endereco
            if self.numero:
                linha += f', {self.numero}'
            if self.complemento:
                linha += f' - {self.complemento}'
            partes.append(linha)
        if self.bairro:
            partes.append(self.bairro)
        if self.cidade and self.estado:
            partes.append(f'{self.cidade}/{self.estado}')
        elif self.cidade:
            partes.append(self.cidade)
        elif self.estado:
            partes.append(self.estado)
        return ', '.join(partes)