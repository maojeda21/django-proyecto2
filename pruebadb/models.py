from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=20)
    fundacion = models.IntegerField()

