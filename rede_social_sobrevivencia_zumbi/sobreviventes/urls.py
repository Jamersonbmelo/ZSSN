from django.urls import path

from rest_framework import routers
from .views import SobreviventeViewSet

router = routers.DefaultRouter()

router.register('sobreviventes', SobreviventeViewSet)

urlpatterns = router.urls

                