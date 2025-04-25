from django.db import models

class Alvo(models.Model):
    identificador = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data_expiracao = models.DateTimeField()

    def __str__(self):
        return f"{self.nome} ({self.identificador})"
