from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Sobrevivente, Item, Votacao
from .serializers import SobreviventeSerializer, ItemSerializer, VotacaoSerializer
# Create your views here.

class SobreviventeViewSet(ModelViewSet):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class VotacaoViewSet(ModelViewSet):
    queryset = Votacao.objects.all()
    serializer_class = VotacaoSerializer