from django.db import models

# Create your models here.

class Programador(models.Model):
    nombre_completo = models.CharField (max_length=100)
    apodo = models.CharField(max_length=50)
    edad = models.SmallIntegerField()
    activo = models.BooleanField(default=True)