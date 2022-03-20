from crypt import methods

from rest_framework.decorators import action
from rest_framework.response import Response
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
    #MODIFICANDO A RESPOSTA DO GET
    def list(self, request, *args, **kwargs):
        return Response({'modificando o GET': 123})
        # isso vaifazer o get rodar essas inhas ao inves do padrão do django
        #basta comentar o list que o metodo vai retornar normalmente os dados do banco padro do django
        #isso é indicado caso vc queimodificar algum parametro enviado

    #MODIFICANDO A RESPOTA DO POST
    def create(self, request, *args, **kwargs):
        return Response({'Modificando o POST': request.data['nome']})


    @action(methods=['get'], detail=True) #se quiser os motivos da denuncia faça um post 
    #esse detail = true é pra informar que precisa de paraemtro na url
    def denunciar(self,request,pk=None):
    #DEPENDENDO DA USA ACTION VC PODE PRECISAR INFORMAR NA UL O ID
        return Response({'DENUNCIA PERSONALIZADA': 'isso é um get entao n tem body'})
