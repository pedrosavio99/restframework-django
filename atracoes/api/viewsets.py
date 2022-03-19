from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracoesViewset(ModelViewSet): #primeiro é preciso criar o serializer 
    #aqui vc chama do banco de dados todos os dados e serializa eles para poder 
    #consumilos na api
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer