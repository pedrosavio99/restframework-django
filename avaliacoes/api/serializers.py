from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'user', 'comentario', 'nota', 'data')


    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # comentario = models.TextField(null=True,blank=True)
    # nota = models.DecimalField(max_digits=3,decimal_places=2)
    # data = models.DateTimeField(auto_now_add=True)
