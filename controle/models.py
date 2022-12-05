from django.db import models

QUITADO = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
 
)



class Usuarios(models.Model):
    
    dia = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=60, blank=True, null=True)
    identidade = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=12, blank=True, null=True)
    valor = models.DecimalField(blank=True, null=True, max_digits = 10, decimal_places = 2)
    observações = models.CharField(max_length=200, blank=True, null=True)
    quitado =  models.CharField(max_length=30, blank=True, null=True, choices=QUITADO)
    poltrona =  models.CharField(max_length=60, blank=True, null=True)
 
    
class Meta:
    ordering = ['poltrona']    

class Gerais(models.Model):   
    congregação = models.CharField(max_length=60, blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    estado = models.CharField(max_length=60, blank=True, null=True)
    data_do_evento = models.DateField(blank=True, null=True)
    valor_da_passagem = models.DecimalField(blank=True, null=True, max_digits = 10, decimal_places = 2)
    quantidade_de_ônibus = models.IntegerField(blank=True, null=True)
    
    
