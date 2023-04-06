from django.db import models

# Create your models here.

class Sobrevivente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(blank = True, null=True)
    sexo = models.CharField(max_length=50)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    infectado = models.BooleanField(default=False)
    
