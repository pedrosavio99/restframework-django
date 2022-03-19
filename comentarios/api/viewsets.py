from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentariosSerializer


class ComentariosViewset(ModelViewSet): #primeiro é preciso criar o serializer 
    #aqui vc chama do banco de dados todos os dados e serializa eles para poder 
    #consumilos na api
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer