from rest_framework import viewsets
from alvos.models.alvo import Alvo
from alvos.api.serializers import AlvoSerializer

class AlvoViewSet(viewsets.ModelViewSet):
    queryset = Alvo.objects.all()
    serializer_class = AlvoSerializer
