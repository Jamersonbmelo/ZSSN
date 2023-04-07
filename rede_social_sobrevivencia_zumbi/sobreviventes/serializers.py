from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Sobrevivente, Item, Votacao


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "nome","pontos"]
        
class SobreviventeSerializer(ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Sobrevivente
        fields = ["id", "nome","idade","sexo", "latitude", "longitude", "infectado","items"]

class VotacaoSerializer(ModelSerializer):
    votante = PrimaryKeyRelatedField(queryset=Sobrevivente.objects.all())
    votado = PrimaryKeyRelatedField(queryset=Sobrevivente.objects.all())