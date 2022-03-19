from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario

class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id','usuario','comentario', 'data', 'aprovado')


    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # comentario = models.TextField()
    # data = models.DateTimeField(auto_now_add=True)
    # aprovado = models.BooleanField(default=True)