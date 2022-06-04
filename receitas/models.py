from django.db import models
from django.forms import CharField
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    enviado_por = models.CharField(max_length=50, default='Desconhecido')
