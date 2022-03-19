from pyexpat import model
from rest_framework.serializers import ModelSerializer

from atracoes.models import Atracao

class AtracaoSerializer(ModelSerializer):
    class Meta :
        model = Atracao
        fields = ('id', 'nome', 'descricao', 'horario_fun', 'idade_minima')


    # nome = models.CharField(max_length=250)
    # descricao = models.TextField()
    # horario_fun = models.TextField()
    # idade_minima = models.IntegerField()
