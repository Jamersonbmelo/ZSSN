from django.urls import path

from rest_framework import routers
from .views import SobreviventeViewSet, ItemViewSet, VotacaoViewSet

router = routers.DefaultRouter()

router.register('sobreviventes', SobreviventeViewSet)
router.register('items', ItemViewSet)
router.register('votacao', VotacaoViewSet)
urlpatterns = router.urls


                