from distutils.command.upload import upload
from django.db import models
from django.forms import CharField
from datetime import datetime
from pessoas.models import Pessoa

class Receita(models.Model):
    enviado_por = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
