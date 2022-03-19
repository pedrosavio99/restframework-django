from pyexpat import model
from rest_framework.serializers import ModelSerializer

from localizacao.models import Localizacao

class LocalizacaoSerializer(ModelSerializer):
    class Meta :
        model = Localizacao
        fields = ('id', 'linha1', 'linha2', 'cidade', 'estado', 'pais')

#    linha1 = models.CharField(max_length=150)
#     linha2 = models.CharField(max_length=150, null=True, blank=True)
#     cidade = models.CharField(max_length=150)
#     estado = models.CharField(max_length=150)
#     pais = models.CharField(max_length=70)


    
