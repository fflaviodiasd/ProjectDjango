from django.db import models
from datetime import datetime


class Reembolso(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    data_servico = models.DateField()
    hora_servico = models.CharField(max_length=20)
    alimentacao = models.BooleanField(default=False)
    combustivel = models.BooleanField(default=False)
    enviado = models.BooleanField(default=False)
    memoria_atend = models.FileField(
        upload_to='memorias_atendimento/%Y/%m/%d/', blank=True)
    rota1 = models.CharField(max_length=200, blank=True, null=True)
    rota2 = models.CharField(max_length=200, blank=True, null=True)
    rota3 = models.CharField(max_length=200, blank=True, null=True)
    rota4 = models.CharField(max_length=200, blank=True, null=True)
    rota5 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "reembolso"
