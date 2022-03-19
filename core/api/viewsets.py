from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet): #primeiro é preciso criar o serializer 
    #aqui vc chama do banco de dados todos os dados e serializa eles para poder 
    #consumilos na api
    #queryset = PontoTuristico.objects.all() #aqui eu irei comentar ess modelo e gerar um filtro logo abaixo
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True) #aqui eu retornei o filtro e 
                #dara um erro pois o django n esta mais encontrando mais o nosso banco pra entrar nesse filtro
                #por isso que em urls da rais preisamos  add a clase base_name na rota de ponto turistico
                #basename='PontoTuristico'