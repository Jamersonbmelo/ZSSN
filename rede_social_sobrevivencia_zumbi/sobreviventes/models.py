from django.db import models

# Create your models here.

class Sobrevivente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(blank = True, null=True)
    sexo = models.CharField(max_length=50)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    infectado = models.BooleanField(default=False)
    items = models.ManyToManyField("Item", blank=True)
    
class Item(models.Model):
    nome = models.CharField(max_length=100)
    pontos = models.IntegerField()
    
class Votacao(models.Model):
    votante = models.ForeignKey(Sobrevivente, on_delete=models.CASCADE, related_name='votos_dados')
    votado = models.ForeignKey(Sobrevivente, on_delete=models.CASCADE, related_name='votos_recebidos')
    data = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('votante', 'votado')