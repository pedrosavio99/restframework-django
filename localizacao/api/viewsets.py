from rest_framework.viewsets import ModelViewSet
from localizacao.models import Localizacao
from .serializers import LocalizacaoSerializer


class LocalizacaoViewset(ModelViewSet): #primeiro é preciso criar o serializer 
    #aqui vc chama do banco de dados todos os dados e serializa eles para poder 
    #consumilos na api
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer