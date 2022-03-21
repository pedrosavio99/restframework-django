from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id','nome','descricao', 'aprovado', 'foto')


    # nome = models.CharField(max_length=150)
    # descricao = models.TextField()
    # aprovado = models.BooleanField(default=False)
    # atracoes = models.ManyToManyField(Atracao)
    # comentarios = models.ManyToManyField(Comentario)
    # avaliacoes = models.ManyToManyField(Avaliacao)
    # localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
