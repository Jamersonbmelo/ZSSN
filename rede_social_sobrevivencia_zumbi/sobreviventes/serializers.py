from rest_framework.serializers import ModelSerializer
from .models import Sobrevivente

class SobreviventeSerializer(ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ["id", "nome","idade","sexo", "latitude", "longitude", "infectado"]

