from django.urls import path, include
from rest_framework.routers import DefaultRouter
from alvos.api.views import AlvoViewSet
from alvos.views import mapa_view

router = DefaultRouter()
router.register(r'alvos', AlvoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', mapa_view, name='mapa'),
]
