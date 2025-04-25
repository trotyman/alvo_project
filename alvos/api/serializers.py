from rest_framework import serializers
from alvos.models import Alvo

class AlvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alvo
        fields = ['id', 'identificador', 'nome', 'latitude', 'longitude', 'data_expiracao']
