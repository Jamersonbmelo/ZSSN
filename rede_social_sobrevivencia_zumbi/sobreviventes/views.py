from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Sobrevivente 
from .serializers import SobreviventeSerializer
# Create your views here.

class SobreviventeViewSet(ModelViewSet):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    
