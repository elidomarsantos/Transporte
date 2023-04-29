
from django.db import models

ADQUIRIU = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
 
)

QUITADO = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
 
)


CARRO = (
    ('01', '01'),
    ('02', '02'),
    ('Outra Congregação', 'Outra Congregação'),
)

class Usuarios(models.Model):
   
    nome = models.CharField(max_length=60, blank=True, null=True)
    identidade = models.BigIntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=12, blank=True, null=True)
    observações = models.CharField(max_length=200, blank=True, null=True)

    

class Gerais_Assembleia(models.Model):   
    congregação = models.CharField(max_length=60, blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    estado = models.CharField(max_length=60, blank=True, null=True)
    data_do_evento = models.DateField(blank=True, null=True)
    valor_da_passagem = models.DecimalField(blank=True, null=True, max_digits = 10, decimal_places = 2)
    coordenador = models.CharField(max_length=60, blank=True, null=True) 
    assistente = models.CharField(max_length=60, blank=True, null=True) 
    
    
class Usuarios_Assembleia(models.Model):   
    nome = models.CharField(max_length=60, blank=True, null=True)
    identidade = models.BigIntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=12, blank=True, null=True)
    observações = models.CharField(max_length=200, blank=True, null=True)
    adquiriu = models.CharField(max_length=30, blank=True, null=True, verbose_name='Solicitou Passagem?', choices=ADQUIRIU)
    quitado = models.CharField(max_length=30, blank=True, null=True, verbose_name='Quitado?', choices=QUITADO)
    poltrona = models.IntegerField(blank=True, null=True)
    carro = models.CharField(max_length=30, blank=True, null=True, choices=CARRO)